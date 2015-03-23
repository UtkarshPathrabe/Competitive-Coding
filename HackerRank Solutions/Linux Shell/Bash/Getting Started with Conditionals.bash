#!/bin/bash

read X
if [ "$X" = 'Y' ]
then
    echo "YES"
elif [ "$X" = 'y' ]
then
    echo "YES"
elif [ "$X" = 'N' ]
then
    echo "NO"
else
    echo "NO"
fi