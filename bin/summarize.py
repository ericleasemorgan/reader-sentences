#!/usr/bin/env python

# summarize.py - use an LLM to summarize the cached results

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public license

# May 23, 2025 - first cut; building my own RAG system
# July 5, 2025 - adding more sophisticated prompts


# configure
MODEL        = 'llama2'
CONTEXT      = './etc/cached-results.txt'
SYSTEMPROMPT = './etc/system-prompt.txt'
PROMPT       = 'Summarize the following context: %s'

# require
from ollama import generate
from sys    import exit

# initialize
context = open( CONTEXT ).read()
system  = open( SYSTEMPROMPT ).read()
prompt  = ( PROMPT % ( context ))

# submit the work, output, and done
try: response = generate( MODEL, prompt, system=system )
except ConnectionError : exit( 'Ollama is probably not running. Start it. Otherwise, call Eric.' )
print( response[ 'response' ] )
exit()
