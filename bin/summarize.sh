#!/usr/bin/env bash

# summarize.sh - a front-end to summarize.py

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 11, 2025 - first cut; deceptively easy


# configure
SUMMARIZE='./bin/summarize.py'

# gussy up the output a bit; sometimes fmt gets in the way
echo
$SUMMARIZE | fmt
echo

# done
exit
