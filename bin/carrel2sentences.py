#!/usr/bin/env python

# carrel2sentences.py - given the name of carrel, cache all of its sentences

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May  26, 2025 - trying yet again
# June 18, 2025 - trapped file too big


# configure
PATTERN   = '*.txt'
COLUMNS   = [ 'item', 'index', 'sentence' ]
MODEL     = 'en_core_web_sm'
CACHE     = 'sentences'
EXTENSION = '.snt'
LIBRARY   = 'localLibrary'

# require
from multiprocessing import Pool
from pandas          import DataFrame
from pathlib         import Path
from rdr             import configuration, TXT
from re              import sub
from shutil          import rmtree
from spacy           import load
from sys             import stderr, argv, exit

# do the work; process the given file
def file2sentences( file, nlp, cache ) :

	# initialize
	item = file.stem
	with open( file ) as handle : text = handle.read()
	
	# debug
	stderr.write( item + '\n' )
	
	# get and normalize sentences
	try : text      = nlp( text )
	except ValueError :
		stderr.write( 'File too big for processor. Call Eric\n' )
		return
		
	sentences = list( text.sents )
	sentences = [ sentence.text                 for sentence in sentences ]	
	sentences = [ sentence.replace( '\t', ' ' ) for sentence in sentences ]
	sentences = [ sentence.replace( '\r', ' ' ) for sentence in sentences ]
	sentences = [ sentence.replace( '\n', ' ' ) for sentence in sentences ]
	sentences = [ sentence.replace( '- ', '' )  for sentence in sentences ]
	sentences = [ sub( ' +', ' ', sentence )    for sentence in sentences ]
	sentences = [ sub( '^ ', '', sentence )     for sentence in sentences ]	
	sentences = [ sub( ' $', '', sentence )     for sentence in sentences ]	

	# process each sentence; create a set of records
	records = []
	for index, sentence in enumerate( sentences ) :
	
		# update the list of records
		records.append( [ item, index + 1 , sentence ] )
			
	# create a dataframe from the records, output, and done
	sentences = DataFrame( records, columns=COLUMNS )
	with open( cache/( item + EXTENSION ), 'w' ) as handle : handle.write( sentences.to_csv( index=False ) )
	
	# done
	return()
	
if __name__ == '__main__':

	# get input
	if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <carrel>" )
	carrel = argv[ 1 ]

	# initialize
	nlp    = load( MODEL )
	carrel = configuration( LIBRARY )/carrel
	files  = list( ( carrel/TXT ).glob( PATTERN ) )
	cache  = carrel/CACHE
	pool   = Pool()
	
	# make sane
	rmtree( cache, ignore_errors=True )
	cache.mkdir()
	
	# submit the work
	pool.starmap( file2sentences, [ [ file, nlp, cache ] for file in files ] )
	
	# clean-up and done
	pool.close()
	exit()