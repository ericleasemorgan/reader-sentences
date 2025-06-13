#!/usr/bin/env python

# index.py - given a carrel, create a database of sentences and their embeddings
# see: https://github.com/asg017/sqlite-vec/

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 16, 2025 - with a lack of hearing, a FOC, and because the CRC machines were under maintence
# May 17, 2025 - migrated to Euclidian (VEC_DISTANCE_L2) distances
# May 22, 2025 - added title of item and item (sentence) number to database


# configure
EMBEDDER  = 'multi-qa-MiniLM-L6-cos-v1'
CREATE    = "CREATE TABLE sentences (title TEXT, item INT, sentence TEXT, embedding FLOAT[384] CHECK (TYPEOF(embedding)=='blob' AND VEC_LENGTH(embedding)==384))"
INSERT    = "INSERT INTO sentences (title, item, sentence, embedding) VALUES (?, ?, ?, ?)"
PATTERN   = '*.txt'
LIBRARY   = 'localLibrary'
INDEXES   = './etc/indexes'
EXTENSION = '.db'

# require
from nltk                  import sent_tokenize
from pathlib               import Path
from rdr                   import TXT, configuration
from re                    import sub
from sentence_transformers import SentenceTransformer
from sqlite_vec            import load
from sqlite3               import connect
from struct                import pack
from sys                   import stderr, argv, exit
from typing                import List

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# serializes a list of floats into a compact "raw bytes" format; makes things more efficient?
def serialize( vector: List[float]) -> bytes : return pack( "%sf" % len( vector ), *vector )

# initialize
stderr.write( "Initializing\n" )
embedder = SentenceTransformer( EMBEDDER )
texts    = configuration( LIBRARY )/carrel/TXT

# (re-)create database
stderr.write( "Creating database\n" )
database = Path( INDEXES )/( carrel + EXTENSION )
database.unlink( missing_ok=True )
database = connect( database )
database.enable_load_extension( True )
load( database )
database.execute( CREATE )

# process each text in the given carrel
stderr.write( "Indexing texts\n" )
count = 0
for file in texts.glob( PATTERN ) :

	# increment and debug
	count += 1
	stderr.write( '  %s (%s)\n' % ( file, str( count ) ) )

	# get the name of the item
	title = file.stem

	# read the given file, tokenize it, and normalize the result
	with open ( file ) as handle : text = handle.read()
	sentences = sent_tokenize( text )
	sentences = [ sentence.replace( '\n', ' ' ) for sentence in sentences ]
	sentences = [ sub( ' +', ' ', sentence )    for sentence in sentences ]
	sentences = [ sub( '^ ', '', sentence )     for sentence in sentences ]
	
	# vectorize the sentences; cpu-intensive
	embeddings = embedder.encode( sentences ).tolist()
	
	# process each sentence/embeddding combination
	item = 0
	for sentence, embedding in zip( sentences, embeddings ) :
		
		# do the inserts
		item = item + 1
		database.execute( INSERT, [ title, item, sentence, serialize( embedding ) ] )	

# commit, close, and done
database.commit()
database.close()
exit()

