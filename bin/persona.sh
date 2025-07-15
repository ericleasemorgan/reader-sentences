#!/usr/bin/env bash

# persona.sh - cache a system prompt based on a persona

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# July 15, 2025 - first cut


# configure
PREFIX='You are '
SUFFIX='.'
PERSONAS='./etc/personas.txt'
SYSTEMPROMPT='./etc/system-prompt.txt'

# initialize
IFS=$'\n'
PERSONAS=( $( cat $PERSONAS ) )
INDEX=0

# display a menu of choices
echo -e "\nThe following personas have been predefined. Choose one:\n"
for PERSONA in "${PERSONAS[@]}"; do

	let "INDEX++"
	echo "  $INDEX. $PERSONA"
	
done

# prompt for, get, and normalize a choice
echo
read -p "Enter a choice: " SELECTION
let "SELECTION--"

# build the prompt and save
SYSTEM=$PREFIX${PERSONAS[$SELECTION]}$SUFFIX
echo $SYSTEM > $SYSTEMPROMPT

# done
echo -e "\nDone. The system will now address summarization and elaboration processes as if it was ${PERSONAS[$SELECTION]}.\n"
exit




