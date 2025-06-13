#!/usr/bin/env bash

# pose-a-question.sh - a front-end to pose-a-question.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 30, 2025 - first cut; last day here at Notre Dame, yikes!


# configure
POSEAQUESTION='./bin/pose-a-question.py'
CACHE='./etc/cached-carrel.txt'

# initialize
CARREL=$( cat $CACHE )

# do the work, output, and done
QUESTION=$( $POSEAQUESTION $CARREL )
echo "While you are waiting, consider the following question: $QUESTION"
exit
