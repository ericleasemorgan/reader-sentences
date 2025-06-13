#!/usr/bin/env bash

# search-with-nouns.sh - yet fifth front-end to search.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 13, 2025 - first cut; in a FOC ("Fit Of Creativity")
# May 14, 2025 - added entitites


# configure
SEARCH='./bin/search.py'

# get input
if [[ -z $1 || -z $2 || -z $3 ]]; then
	echo "Usage: $0 <carrel> <breadth> <depth>" >&2
	exit
fi
CARREL=$1
SIZE=$2
DEPTH=$3

# use the Reader to get SIZE number of keywords and build a query
QUERY=$(rdr pos $CARREL -c -s words -l N | head -n $SIZE | cut -f1 | tr '\n' ' ')
echo "    Query: $QUERY" >&2

# build a pattern
PATTERN="\b$(echo $QUERY | sed "s/ /\\\b|\\\b/g")\b"
echo "  Pattern: $PATTERN" >&2

# submit the work, format the output, and done
$SEARCH $CARREL "$QUERY" $DEPTH | sed "s/$/\n/" | fold -s | less -i --pattern=$PATTERN
exit
