#!/usr/bin/env python

# elaborate.py - given set of cached content and a query, address the query

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# May 23, 2025 - first cut; building my own RAG system


# configure
MODEL   = 'llama2'
CONTEXT = './etc/cached-results.txt'
PROMPT  = 'In a few short short sentences, address the question %s using the following context: %s'

# require
from ollama import generate
from sys    import argv, exit

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <question>" )
question = argv[ 1 ]

# initialize
context = open( CONTEXT ).read()
prompt  = ( PROMPT % ( question, context ))

# submit the work, output, and done
result = generate( MODEL, prompt )
print( result['response'] )
exit()
