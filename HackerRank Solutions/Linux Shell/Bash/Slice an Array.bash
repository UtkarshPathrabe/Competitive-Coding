#!/bin/bash

arr=($(cat))
echo ${arr[@]:3:5}