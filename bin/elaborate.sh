#!/usr/bin/env bash

# elaborate.sh - a front-end to elaborate.py

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 11, 2025 - first cut; deceptively easy


# configure
ELABORATE='./bin/elaborate.py'

if [[ -z $1 ]]; then
	echo "Usage: $0 <query>" >&2
	exit
fi
QUERY=$1

# gussy up the output a bit
echo
echo
$ELABORATE "$QUERY" | fmt
echo

# done
exit
