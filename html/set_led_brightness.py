import RPi.GPIO as G
import sys
from time import sleep
from threading import Timer


# set up gpio
G.setmode(G.BCM)
G.setwarnings(False)
G.setup(27, G.OUT)
fan_pwm = G.PWM(27, 500)
fan_pwm.start(0)

file_read_write = open("on_off_variable.txt", "w+")
file_read_write.write("0")
file_read_write.close()

prev_val = 0


def on_off_file_checker():
	Timer(0.1, on_off_file_checker).start()
	f = open("on_off_variable.txt", "r")
	file_val = int(f.read())
	set_value(file_val)


def set_value(on_off_val):
	global prev_val

	if on_off_val == 1:
		
		f = open("brightness_variable.txt", "r")
		file_val = int(f.read())
		
		if prev_val != file_val:
			change_brightness(file_val)
			prev_val = on_off_val
			
	elif on_off_val == 0:
		change_brightness(0)


def change_brightness(brightness_var):

	if brightness_var == 0:
		fan_pwm.ChangeDutyCycle(0)

	elif brightness_var == 2:
		fan_pwm.ChangeDutyCycle(25)

	elif brightness_var == 3:
		fan_pwm.ChangeDutyCycle(50)

	elif brightness_var == 4:
		fan_pwm.ChangeDutyCycle(100)

on_off_file_checker()

while True:
	sleep(0.1)
	continue
