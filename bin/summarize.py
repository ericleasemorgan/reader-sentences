#!/usr/bin/env python

# summarize.py - use an LLM to summarize the cached results

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# May 23, 2025 - first cut; building my own RAG system
# July 5, 2025 - adding more sophisticated prompts


# configure
MODEL   = 'llama2'
CONTEXT = './etc/cached-results.txt'
PROMPT  = 'In a few short sentences, summarize the following context: %s'
SYSTEM  = 'You are a college professor of few words.'

# require
from ollama import generate
from sys    import exit

# initialize
context = open( CONTEXT ).read()
prompt  = ( PROMPT % ( context ))

# submit the work, output, and done
try: response = generate( MODEL, prompt, system=SYSTEM )
except ConnectionError : exit( 'Ollama is probably not running. Start it. Otherwise, call Eric.' )
print( response[ 'response' ] )
exit()
