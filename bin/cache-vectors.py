#!/usr/bin/env python

# vectorize.py - given a previously vectorized carrel, cache the vectors to a file

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# March 31, 2026 - first cut; practicing going slower


# configure
DATABASE = 'sentences.db'
SELECT   = 'SELECT vector FROM sentences'
LIBRARY  = 'localLibrary'
VECTORS  = 'vectors.pkl'
CACHE    = 'etc'

# require
from sqlite3  import connect
from numpy    import array
from rdr      import configuration, ETC
from pathlib  import Path
from pickle   import dump
from sys      import argv, exit

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# initialize
connection = connect( Path( configuration( LIBRARY )/carrel/ETC/DATABASE ) )
cursor     = connection.cursor()

# search and process each result; create a list of vectors
vectors = []
cursor.execute( SELECT )
for result in cursor.fetchall() : vectors.append( eval( result[ 0 ] ) )
	
# transform the vectors (a list of lists) into a numpy array
vectors = array( vectors )

# cache and done
with open( Path( CACHE )/VECTORS, 'wb' ) as handle : dump( vectors, handle )
exit()
