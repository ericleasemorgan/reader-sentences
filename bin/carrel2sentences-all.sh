#!/usr/bin/env bash

# carrel2sentences-all.sh - cache sentences for all carrels

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 28, 2025 - first cut


# configure
CARREL2SENTENCES='./bin/carrel2sentences.py'
SENTENCES='sentences'

# initialize
LIBRARY=$( rdr get )
CARRELS=$( rdr catalog )

# process each carrel
for CARREL in ${CARRELS[@]}; do

	# re=initialize
	CACHE=$LIBRARY/$CARREL/$SENTENCES
	
	# check; do not do the work if it has already been don
	if [[ -d $CACHE ]]; then continue; fi

	# do the work
	$CARREL2SENTENCES $CARREL
	
# fini
done
exit