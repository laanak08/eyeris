#!/bin/bash
#for COPY in '003' '004' '009' '010' '011' '017' '018' 
#for COPY in '003' '004' '009' '010' '011' '012' '013' '005'
for COPY in '003' '004' '009' '010' '011' '012' '017'
do
	echo 1 > /cpm/projects/smapi/state/state_${COPY}.txt
	echo "Starting copy ${COPY}"
	/cpm/projects/smapi/bin/readrawfile3_7.py ${COPY} >> /cpm/projects/smapi/logs/cron_${COPY}.log 2>&1 &
	sleep 6
done
#for COPY in '019' '020' 
#do
	#echo 1 > /cpm/projects/smapi/state/state_${COPY}.txt
	#echo "Starting copy ${COPY}"
	#/cpm/projects/smapi/bin/readrawfile3_1C.py ${COPY} >> /cpm/projects/smapi/logs/cron_${COPY}.log 2>&1 &
	#sleep 6
#done
