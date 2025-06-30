#!/usr/bin/env python

# summarize.py - use an LLM to summarize the cached results

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# May 23, 2025 - first cut; building my own RAG system


# configure
MODEL   = 'llama2'
CONTEXT = './etc/cached-results.txt'
PROMPT  = 'Summarize the following context: %s'

# require
from ollama import generate
from sys    import exit

# initialize
context = open( CONTEXT ).read()
prompt  = ( PROMPT % ( context ))

# submit the work, output, and done
try: response = generate( MODEL, prompt )
except ConnectionError as error : exit( 'Ollam is probably not running. Start it.' )
print( response[ 'response' ] )
exit()
