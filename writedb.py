import argparse
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import time
import random
import json
import paho.mqtt.client as mqtt

USER = 'root'
PASSWORD = 'root'
DBNAME = 'mydb'
HOST = 'localhost'
PORT = 8086
dbclient = None

mqtt_broker = "m2m.eclipse.org"
topic = "iotp/tph"
my_mqtt = None

sensorData = 0

def main():
	dbclient = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)
	startMQTT()
	while True:
		if sensorData:
			data_point = getSensorData()
			dbclient.write_points(data_point)
			print(data_point)
			print("Written data")
			time.sleep(2)

def getSensorData():
	now = time.gmtime()
	pointValues = [
		{
			"time": time.strftime("%Y-%m-%d %H:%M:%S", now),
			"measurement": 'reading',
			"tags": {
				"nodeId": "node_1",
			},
			"fields": {
				"value": sensorData
			},	
		}
	]

	return(pointValues)

def onMessage(client, userdata, message):
	global sensorData
	#print("%s %s" % (message.topic, message.payload))
	m_decode=str(message.payload.decode("utf-8","ignore"))
	tph = json.loads(m_decode)
		
	sensorData = tph[0]
	
def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic, qos=1)
	#my_mqtt.subscribe(topic_vmem, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to topic")

if __name__ == '__main__':
	main()