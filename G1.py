import RPi.GPIO as G
import sys
import time as t
import threading

# set up gpio
G.setmode(G.BCM)
G.setwarnings(False)
G.setup(27,G.OUT)
p = G.PWM(27, 500)
p.start(0)

f= open("var.txt","w+")
f.write("1")
f.close()
globalVal = 1
brightnessVar = 1

def foo():
	threading.Timer(0.1, foo).start()
	global brightnessVar
	f= open("var.txt","r")
	brightnessVar =int(f.read())
	setValue(brightnessVar)

def setValue(val):
    global globalVal
    valueChanged= globalVal != val
    if valueChanged:
        changeBrightness()
        globalVal = val
		
def changeBrightness():
	if(brightnessVar == 1):
		p.ChangeDutyCycle(25)
		
	elif(brightnessVar == 2):
		p.ChangeDutyCycle(50)
		
	elif(brightnessVar == 3):
		p.ChangeDutyCycle(100)
		
	elif(brightnessVar == 4):
		p.stop()
		G.cleanup()
		f= open("var.txt","w")
		f.write("1")
		f.close()
		print("Exited")
		exit()
foo()

while True:
	t.sleep(0.1)
	continue
