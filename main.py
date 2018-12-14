import bme280
import time
import paho.mqtt.client as mqtt
import json

mqtt_broker = "m2m.eclipse.org"
topic = "iotp/tph"
 
while True:
 
	# temperature,pressure,humidity = bme280.readBME280All()
	tph = bme280.readBME280All()
	 
	#print (tph)
	
	payload = json.dumps(tph)
	
	my_mqtt = mqtt.Client()
	print("\nCreated client object at "+ time.strftime("%H:%M:%S"))
	
	my_mqtt.connect(mqtt_broker, port=1883)
	print("--connected to broker")
	
	try:
		#my_mqtt.publish(topic, pay_load)
		my_mqtt.publish(topic,payload)
		print(payload)
		
		time.sleep(1)
		
	except:
		print("--error publishing!")
		
	else:
		my_mqtt.disconnect()
		print("--disconnected from broker")
