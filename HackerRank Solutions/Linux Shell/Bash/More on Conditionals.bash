#!/bin/bash

read X
read Y
read Z
if [ "$X" -eq "$Y" ]
then
    if [ "$X" -eq "$Z" ]
    then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
elif [ "$Y" -eq "$Z" ]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi    