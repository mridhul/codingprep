#!/bin/bash

tail -1 rmid.log|while read line;do
	linePID=`echo ${line} |awk {'print $1'}`  # Get process ID
	rmIDVal=`echo ${line} |awk {'print $3'}`  # Get RMID size
	if [ $rmIDVal -gt 30 ];then
		echo "${linePID}"
	fi
done

