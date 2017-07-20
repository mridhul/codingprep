#!/bin/bash

total=0

read N
for ((i=1;i<=$N;i++))
do
	read numbers
	total=`expr $total + $numbers`
done

printf "%.3f" $(bc -l <<< "$total/$N")