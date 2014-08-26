#! /bin/bash

bcm2wir_map=(
-1 -1  8  9  7
-1 -1 11 10 13
12 14 -1 -1 15
16 -1  0  1 -1
-1 -1  3  4  5
 6 -1  2 
)

if [ $# != 1 ]; then
	echo "Please input gpio num."
	exit 1
fi

if [ $1 -lt 0 -o $1 -gt 27 ]; then
	echo "The input gpio num is not valid."
	exit 1
fi

gpio=${bcm2wir_map[$1]}
if [ $gpio -eq -1 ]; then
	echo "The input gpio num is not valid."
	exit 1
fi

echo $gpio

