#!/usr/bin/env bash

# format.sh - a front-end to format.py

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 11, 2025 - first cut; deceptively easy


# configure
FORMAT='./bin/format.py'

# gussy up the output a bit
echo
echo
$FORMAT | fmt
echo

# done
exit
