import RPi.GPIO as G
import sys
import time as t
import threading

# set up gpio
G.setmode(G.BCM)
G.setwarnings(False)
G.setup(27, G.OUT)
p = G.PWM(27, 500)
p.start(0)

file_read_write = open("on_off_variable.txt", "w+")
file_read_write.write("0")
file_read_write.close()
prev_val = 0


def foo():
	threading.Timer(0.1, foo).start()
	f = open("on_off_variable.txt", "r")
	file_val = int(f.read())
	set_value(file_val)


def set_value(val):
	global prev_val

	if val == 1:
		
		f = open("brightness_variable.txt", "r")
		file_val = int(f.read())
		
		if prev_val != file_val:
			change_brightness(file_val)
			prev_val = val
			
	elif val == 0:
		change_brightness(0)


def change_brightness(brightness_var):

	if brightness_var == 0:
		p.ChangeDutyCycle(0)

	elif brightness_var == 2:
		p.ChangeDutyCycle(25)

	elif brightness_var == 3:
		p.ChangeDutyCycle(50)

	elif brightness_var == 4:
		p.ChangeDutyCycle(100)

foo()

while True:
	t.sleep(0.1)
	continue
