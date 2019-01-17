import RPi.GPIO as G
import sys
import time as t

# get and type cast second argument to int
first_arg = int(sys.argv[1])

# set up gpio
G.setmode(G.BCM)
G.setwarnings(False)
G.setup(27,G.OUT)
p = G.PWM(27, 1000)

print(first_arg)

# if first_arg is one, on led
if(first_arg == 1):
	p.start(100)
	while True:
		continue
	
# if zero, off led
elif(first_arg == 0):
	p.start(0)
	while True:
		continue
	
# if three, exit python script and clean up
elif(first_arg == 3):
	G.cleanup()
	print("Exited")
	exit()
