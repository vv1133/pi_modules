#! /bin/bash

key=(KEY_OK KEY_POWER KEY_MUTE KEY_VOLUMEDOWN KEY_VOLUMEUP KEY_UP KEY_DOWN KEY_CANCEL KEY_TAB)

function print_help()
{
	echo "please input one of the following keys:"
	for k in ${key[@]}; do
		echo $k
	done
}

function check_key()
{
	for k in ${key[@]}; do
		if [ $k = $1 ]; then
			return 1
		fi
	done
	return 0
}


if [ $# != 1 ]; then
	echo "args error!"
	print_help
	exit 1
fi

check_key $1
if [ $? = 0 ]; then
	echo "$1 is not a valid key"
	print_help
	exit 1
fi

irsend SEND_ONCE tv_lircd.conf $1
echo "send $1 ok"
