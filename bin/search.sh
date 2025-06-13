#!/usr/bin/env bash

# search.sh - a front-end to search.py

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 11, 2025 - first cut; deceptively easy


# configure
SEARCH='./bin/search.py'

if [[ -z $1 || -z $2 || -z $3 ]]; then
	echo "Usage: $0 <carrel> <query> <depth>" >&2
	exit
fi
CARREL=$1
QUERY=$2
DEPTH=$3

# gussy up the output a bit
echo
$SEARCH $CARREL "$QUERY" $DEPTH | sed s"/$/ /" | fmt
echo

# done
exit
