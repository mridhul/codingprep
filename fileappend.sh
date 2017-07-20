#!/bin/bash

for word in `cat file1.txt`;do
	res=$(grep $word file2.txt)
	if [ -z ${res} ];then
		echo $word >> file2.txt
	fi
done