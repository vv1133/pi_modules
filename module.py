#! /usr/bin/python

import subprocess
import sys
import os

table = [ \
			{"name":"send_ir", "gpio":25, "shared":"F", "path":"send_tv_code/send.sh", \
				"info":"Send infra-red signals."}, \
			{"name":"recv_ir", "gpio":18, "shared":"T", "path":None, \
				"info":"Receive infra-red signals."}, \
			{"name":"dht11", "gpio":4, "shared":"F", "path":"dht11/dht11.sh", \
				"info":"Get temperature and humidity."}, \
			{"name":"detect_sound", "gpio":5, "shared":"F", "path":"sound_detect/detect.sh", \
				"info":"Detect sound."}, \
			{"name":"send_rc", "gpio":17, "shared":"F", "path":"rcswitch-pi/send.sh", \
				"info":"Send 315M rc signals."}, \
			{"name":"detect_sensor", "gpio":7, "shared":"F", "path":"human_sensor/detect.sh", \
				"info":"Detect human sensor."}, \
			{"name":"buzzer", "gpio":8, "shared":"F", "path":"buzzer/buzzer.sh", \
				"info":"Make buzzer sound."}, \
		]


def check_table():
	global table
	num_map = [False for i in range(30)]
	for member in table:
		if member["shared"] == "F":
			if num_map[member["gpio"]] == True:
				print "conflict: %d" %member["gpio"]
				print_table()
			num_map[member["gpio"]] = True

def print_table():
	global table
	print "%14s %4s %6s %s" %("NAME", "GPIO", "SHARED", "INFO")
	for member in table:
		print "%14s %4d %6s %s" %(member["name"], member["gpio"], member["shared"], member["info"])

def execute(name, args):
	global table
	path = ""
	for member in table:
		if member["name"] == name:
			path = member["path"]
			gpio = member["gpio"]
			break

	if path == "":
		print "no such name: %s" %name
		return

	cmd = ["/home/pi/pi_modules/" + path]
	cmd.extend(args)
	cmd.extend([str(gpio)])
	#print cmd
	try:
		p = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print p.stdout.read()
	except:
		print "warning: subprcess failed"
		sys.exit(1)


if len(sys.argv) > 1:
	execute(sys.argv[1], sys.argv[2:])
else:
	check_table()
	print_table()

