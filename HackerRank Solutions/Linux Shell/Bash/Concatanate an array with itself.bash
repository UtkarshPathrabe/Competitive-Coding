#!/bin/bash

arr=($(cat))
arr=(${arr[@]} ${arr[@]} ${arr[@]})
echo ${arr[@]}