#!/usr/bin/python3
from flask import Flask, jsonify
import RPi.GPIO as G
#from gpiozero import PWMLED as pwmled
import time as t

G.setwarnings(False)           #do not show any warnings

G.setmode(G.BCM)
G.setup(27, G.OUT)

p = G.PWM(27,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle

#led = pwmled(27)

app = Flask(__name__)

light_on = False

def changePWM(dc):
	p.ChangeDutyCycle(dc)
	
@app.route("/")
def hello():
	return "Hello World"

@app.route("/ctrl/fan/on/<int:speed>", methods=['GET'])
def on_fan_speed(speed):
	changePWM(speed)
	return "Fan speed: " + str(speed)
	
		
@app.route("/ctrl/fan/on", methods=['GET'])
def on_fan():
	G.output(27, True)
	return "Fan is on"
	
@app.route("/ctrl/fan/off", methods=['GET'])
def off_fan():
	G.output(27, False)
	light_on = False
	return "Fan is off"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
