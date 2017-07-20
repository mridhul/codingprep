#!/bin/bash

declare -a alist=(4,5,7,8,9)

hasdup="True"

for ((i=0;i<${#alist[@]};i++));do
	if alist[i]==alist[i+1];then
		hasdup="False"
	fi

done
echo ${hasdup}

