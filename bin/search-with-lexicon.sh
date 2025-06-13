#!/usr/bin/env bash

# search-with-lexicon.sh - yet another another front-end to search.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 21, 2025 - more and more


# configure
SEARCH='./bin/search.py'
ETC='etc'
LEXICON='lexicon.txt'
DEPTH=64

# get input
if [[ -z $1|| -z $2 ]]; then
	echo "Usage: $0 <carrel> <terse|short|brief|long|verbose>" >&2
	exit
fi
CARREL=$1
SIZE=$2

if [[ "$SIZE" == 'terse' ]]; then
	DEPTH=8
elif [[ "$SIZE" == 'short' ]]; then
	DEPTH=16
elif [[ "$SIZE" == 'brief' ]]; then
	DEPTH=32
elif [[ "$SIZE" == 'long' ]]; then
	DEPTH=64
elif [[ "$SIZE" == 'verbose' ]]; then
	DEPTH=128
else
	DEPTH=32
fi

# use the Reader to get SIZE number of keywords and build a query
LEXICON="$(rdr get)/$CARREL/$ETC/$LEXICON"
QUERY=$(cat $LEXICON | tr '\n' ' ')

# build a pattern
PATTERN="\b$(echo $QUERY | sed "s/ /\\\b|\\\b/g")\b"
echo "  Pattern: $PATTERN" >&2

# submit the work, format the output, and done
$SEARCH $CARREL "$QUERY" $DEPTH | sed "s/$/\n/" | fold -s | less -i --pattern=$PATTERN
exit
