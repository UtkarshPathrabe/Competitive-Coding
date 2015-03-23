#!/bin/bash

read N
Total=0
for i in $(seq 1 $N)
do
	read X
	Total=$((Total + X))
done
printf "%.3f\n" $(echo "$Total / $N" | bc -l)