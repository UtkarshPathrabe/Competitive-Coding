#!/bin/bash

arr=($(cat))
declare -a pattern1=( ${arr[@]/*a*/} )
declare -a pattern2=( ${pattern1[@]/*A*/} )
echo ${pattern2[@]}