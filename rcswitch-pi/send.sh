#! /bin/bash

dir=`dirname $0`
pin=0

if [ ! -z $1 ]; then
	pin=`./bcm2wiring.sh $1`
fi

sudo $dir/send 11111 4 1 $pin
