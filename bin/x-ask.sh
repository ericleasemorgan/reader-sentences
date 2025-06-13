#!/usr/bin/env bash

# search.sh - a front-end to search.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May  13, 2025 - first cut; in a FOC ("Fit Of Creativity")
# June  6, 2025 - added sizes


# configure
SEARCH='./bin/search.py'

# get input
if [[ -z $1  || -z $2 || -z $3 ]]; then
	echo "Usage: $0 <carrel> <query> <terse|short|brief|long|versbose>" >&2
	exit
fi
CARREL=$1
QUERY=$2
SIZE=$3

# initialize
if   [[ "$SIZE" == 'terse'   ]]; then DEPTH=1
elif [[ "$SIZE" == 'short'   ]]; then DEPTH=4
elif [[ "$SIZE" == 'brief'   ]]; then DEPTH=8
elif [[ "$SIZE" == 'long'    ]]; then DEPTH=16
elif [[ "$SIZE" == 'verbose' ]]; then DEPTH=32
else                                  DEPTH=8
fi

# debug
clear
echo
echo
echo "$QUERY" >&2
echo

# submit the work, format the output, and done
$SEARCH $CARREL "$QUERY" $DEPTH | fmt 
echo
