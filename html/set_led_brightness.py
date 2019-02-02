# import necessary packages
import RPi.GPIO as G
from time import sleep
from threading import Timer


# set up gpio
G.setmode(G.BCM)
G.setwarnings(False)
G.setup(27, G.OUT)
fan_pwm = G.PWM(27, 500)
fan_pwm.start(0)

# reset on_off_variable.txt file
file_read_write = open("on_off_variable.txt", "w+")
file_read_write.write("0")
file_read_write.close()

# initialise prev_val variable
prev_val = 0


# function with looping timer interrupt to check on_off_variable.txt file
def on_off_file_checker():

	# reload timer
	Timer(0.1, on_off_file_checker).start()

	# read on_off_variable.txt file
	f = open("on_off_variable.txt", "r")
	file_val = int(f.read())

	# run function with read value
	set_value(file_val)


def set_value(on_off_val):
	global prev_val

	if on_off_val == 1:

		# read brightness_variable.txt file
		f = open("brightness_variable.txt", "r")
		file_val = int(f.read())

		# if value changed
		if prev_val != file_val:

			# set led brightness
			change_brightness(file_val)

			# set previous value
			prev_val = on_off_val
			
	elif on_off_val == 0:

		# off led
		change_brightness(0)


# function to change led brightness to varying duty cycles
def change_brightness(brightness_var):

	if brightness_var == 0:
		fan_pwm.ChangeDutyCycle(0)

	elif brightness_var == 2:
		fan_pwm.ChangeDutyCycle(25)

	elif brightness_var == 3:
		fan_pwm.ChangeDutyCycle(50)

	elif brightness_var == 4:
		fan_pwm.ChangeDutyCycle(100)


# start function loop
on_off_file_checker()

while True:
	sleep(0.1)
	continue
