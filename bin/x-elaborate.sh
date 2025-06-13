#!/usr/bin/env bash

# elaborate.sh - a front-end to elaborate.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 13, 2025 - first cut; in a FOC ("Fit Of Creativity")


# configure
CACHECONTEXT='./bin/cache-context.sh'
ELABORATE='./bin/elaborate.py'

# get input
if [[ -z $1  || -z $2 ]]; then
	echo "Usage: $0 <carrel> <query>" >&2
	exit
fi
CARREL=$1
QUERY=$2

# cache context
$CACHECONTEXT $CARREL "$QUERY"

# address the question, output, and done
RESONSE=$($ELABORATE "$QUERY")
echo $RESONSE | fold -s
echo >&2
exit