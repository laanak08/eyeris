#!/bin/bash
for COPY in '003' '004' '009' '010' '011' '012' '013' '016' '017' '018' '019' '020' '005'
do
	echo 0 > /cpm/projects/smapi/state/state_${COPY}.txt
done
