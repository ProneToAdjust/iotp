import smbus2
import bme280
import time
import paho.mqtt.client as mqtt
import json

mqtt_broker = "m2m.eclipse.org"
topic = "iotp/tph"

port = 1
address = 0x76
bus = smbus2.SMBus(port)

tph = [None,None,None]

calibration_params = bme280.load_calibration_params(bus, address)
 
while True:
 
	data = bme280.sample(bus, address, calibration_params)
	
	tph[0] = data.temperature
	tph[1] = data.pressure
	tph[2] = data.humidity
	
	payload = json.dumps(tph)
	
	my_mqtt = mqtt.Client()
	print("\nCreated client object at "+ time.strftime("%H:%M:%S"))
	
	my_mqtt.connect(mqtt_broker, port=1883)
	print("--connected to broker")
	
	try:
		my_mqtt.publish(topic,payload)
		print(payload)
		
		time.sleep(1)
		
	except:
		print("--error publishing!")
		
	else:
		my_mqtt.disconnect()
		print("--disconnected from broker")
