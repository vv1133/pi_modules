#!/bin/bash

gpio=7
if [ ! -z $1 ]; then
	gpio=$1
fi

dir=`dirname $0`
sudo $dir/detect $gpio

