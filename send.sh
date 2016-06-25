#!/bin/bash

DIR=/tmp
COUNTER=0
FILE=raw.jpg
SLEEP_SEC="0.02"
WAIT_SEC=5
WAIT_THRES=$(echo "$WAIT_SEC/$SLEEP_SEC" | bc )

while true; do
	if [ -f $DIR/$FILE ]; then
		(( COUNTER++ ))
		WAIT_COUNTER=0
		scp $DIR/$FILE root@192.241.244.189:/var/www/html &> /dev/null
		echo "image $COUNTER sent to processing server at $(date)"
		rm -f $DIR/$FILE &> /dev/null
		echo "image $COUNTER deleted from camera server"	
	else 
		(( WAIT_COUNTER++ ))
	fi

	if [ $WAIT_COUNTER -gt $WAIT_THRES ]; then
		echo "Camera is waiting IO..."
		WAIT_COUNTER=0
	fi

	sleep $SLEEP_SEC

done
