#!/usr/bin/env python

# search.py - given a carrel and a query, return similar sentences
# see: 
#   https://github.com/asg017/sqlite-vec/
#   https://github.com/asg017/sqlite-vec/blob/main/examples/simple-python/demo.py
#   https://github.com/asg017/sqlite-vec/issues/116

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 16, 2025 - with a lack of hearing, a FOC, and becuase the CRC machines were under maintence
# May 17, 2025 - migrated to Euclidian (VEC_DISTANCE_L2) distances
# May 30, 2025 - added cache; tomorrow is my last day here at Notre Dame, yikes!


# configure
EMBEDDER  = 'multi-qa-MiniLM-L6-cos-v1'
SELECT    = "SELECT sentence, VEC_DISTANCE_L2(embedding, ?) AS distance FROM sentences ORDER BY distance, title, item LIMIT ?"
INDEXES   = './etc/indexes'
EXTENSION = '.db'
DATABASE  = 'sentences.db'
LIBRARY   = 'localLibrary'
RESULTS   = './etc/cached-results.txt'
CARREL    = './etc/cached-carrel.txt'

# require
from pathlib               import Path
from rdr                   import configuration, ETC
from sentence_transformers import SentenceTransformer
from sqlite_vec            import load
from sqlite3               import connect
from struct                import pack
from sys                   import stderr, argv, exit
from typing                import List

# serializes a list of floats into a compact "raw bytes" format; makes things more efficient?
def serialize( vector: List[float]) -> bytes : return pack( "%sf" % len( vector ), *vector )

# get input
if len( argv ) != 4 : exit( 'Usage: ' + argv[ 0 ] + " <carrel> <query> <depth>" )
carrel = argv[ 1 ]
query  = argv[ 2 ]
depth  = argv[ 3 ]

# initialize
embedder = SentenceTransformer( EMBEDDER )
database = connect( configuration( LIBRARY )/carrel/ETC/DATABASE )
database.enable_load_extension( True )
load( database )

# cache the carrel
with open( CARREL, 'w' ) as handle : handle.write( carrel )

#  vectorize query, search, output, and done
query   = embedder.encode( query ).tolist()
records = database.execute( SELECT, [ serialize( query ), depth ] ).fetchall()
cache   = []
for record in records :

	# update the cache
	cache.append( record[ 0 ] )
	
	# output
	print( record[ 0 ] )
	
# output some more and done
with open( RESULTS, 'w' ) as handle : handle.write( '\n'.join( cache ) )
exit()
