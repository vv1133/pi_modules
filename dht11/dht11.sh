#!/bin/bash

gpio=4
if [ ! -z $1 ]; then
        gpio=$1
fi

dir=`dirname $0`
sudo $dir/Adafruit_DHT 11 $gpio

