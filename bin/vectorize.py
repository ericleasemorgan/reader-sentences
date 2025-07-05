#!/usr/bin/env python

# vectorize.py - given a carrel, create a database of sentences and their embeddings
# see: https://github.com/asg017/sqlite-vec/

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 16, 2025 - with a lack of hearing, a FOC, and because the CRC machines were under maintence
# May 17, 2025 - migrated to Euclidian (VEC_DISTANCE_L2) distances
# May 22, 2025 - added title of item and item (sentence) number to database
# June 7, 2025 - normalized sentences so they are always strings
# July 4, 2025 - using a new embedder; actually moved to Ollama


# configure
MODEL    = 'nomic-embed-text'
CREATE   = "CREATE TABLE sentences (title TEXT, item INT, sentence TEXT, embedding FLOAT[768] CHECK (TYPEOF(embedding)=='blob' AND VEC_LENGTH(embedding)==768))"
INSERT   = "INSERT INTO sentences (title, item, sentence, embedding) VALUES (?, ?, ?, ?)"
PATTERN  = '*.snt'
LIBRARY  = 'localLibrary'
DATABASE = 'sentences.db'
CACHE    = 'sentences'

# require
from ollama     import embed
from pandas     import read_csv
from pathlib    import Path
from rdr        import configuration, ETC
from re         import sub
from sqlite_vec import load
from sqlite3    import connect
from struct     import pack
from sys        import stderr, argv, exit
from typing     import List

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# serializes a list of floats into a compact "raw bytes" format; makes things more efficient?
def serialize( vector: List[ float ] ) -> bytes : return pack( "%sf" % len( vector ), *vector )

# initialize
stderr.write( "Initializing\n" )
cache = configuration( LIBRARY )/carrel/CACHE

# (re-)create database
stderr.write( "Creating database\n" )
database = configuration( LIBRARY )/carrel/ETC/DATABASE
database.unlink( missing_ok=True )
database = connect( database )
database.enable_load_extension( True )
load( database )
database.execute( CREATE )

# process each text in the given carrel
stderr.write( "Indexing texts\n" )
count = 0
for file in cache.glob( PATTERN ) :
	
	# increment and debug
	title =  file.stem
	count += 1
	stderr.write( '  %s (%s)\n' % ( file, str( count ) ) )
		
	# re-initialize and normalize
	sentences = list( read_csv( file )[ 'sentence' ] )
	sentences = [ str( sentence ) for sentence in sentences ]
	
	# vectorize the sentences; cpu-intensive
	embeddings = embed( model=MODEL, input=sentences ).model_dump( mode='json' )[ 'embeddings' ]

	# process each sentence/embeddding combination
	item = 0
	for sentence, embedding in zip( sentences, embeddings ) :
		
		# do the inserts
		item += 1
		database.execute( INSERT, [ title, item, sentence, serialize( embedding ) ] )	

# commit, close, and done
database.commit()
database.close()
exit()

