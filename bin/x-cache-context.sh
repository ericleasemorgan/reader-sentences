#!/usr/bin/env bash

# cache-context.sh - do a vector search and save the results

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 23, 2025 - first cut; fun!


# configure
SEARCH='./bin/search.py'
DEPTH=32
CACHE='./etc/context.txt'

# get input
if [[ -z $1  || -z $2 ]]; then
	echo "Usage: $0 <carrel> <query>" >&2
	exit
fi
CARREL=$1
QUERY=$2

# do the work and format the results
SENTENCES=$( $SEARCH $CARREL "$QUERY" $DEPTH )
CONTEXT=$( echo $SENTENCES | sed "s/\n/ /" )

# debub
echo                       >&2
echo "   carrel: $CARREL"  >&2
echo "    query: $QUERY"   >&2
echo "  context: $CONTEXT" >&2
echo                       >&2

# output and done
echo $CONTEXT > $CACHE
exit
