#!/usr/bin/env bash

# vectorize-all.sh - index all cached sentences for all carrels

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# June 28, 2025 - first cut


# configure
VECTORIIZE='./bin/vectorize.py'
DATABASE='sentences.db'
ETC='etc'

# initialize
LIBRARY=$( rdr get )
CARRELS=$( rdr catalog )

# process each carrel
for CARREL in ${CARRELS[@]}; do

	# re=initialize
	CACHE=$LIBRARY/$CARREL/$ETC/$DATABASE
	
	# check; do not do the work if it has already been don
	if [[ -f $CACHE ]]; then continue; fi

	# do the work
	$VECTORIIZE $CARREL
	
# fini
done
exit