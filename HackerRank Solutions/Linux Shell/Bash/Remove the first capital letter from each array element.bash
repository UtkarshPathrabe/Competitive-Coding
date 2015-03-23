#!/bin/bash

i=1
while read word           
do          
    words[i]=$word
    i=$(( $i + 1 ))
done
echo ${words[@]/[A-Z]/.}