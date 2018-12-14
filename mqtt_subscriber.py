import time
import json
import paho.mqtt.client as mqtt

mqtt_broker = "m2m.eclipse.org"
topic_cpu = "iotp/tph"
my_mqtt = None

def onMessage(client, userdata, message):
	#print("%s %s" % (message.topic, message.payload))
	m_decode=str(message.payload.decode("utf-8","ignore"))
	tph = json.loads(m_decode)
	for x in tph:
		print (x)

def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic_cpu, qos=1)
	#my_mqtt.subscribe(topic_vmem, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to topic")
	
def main():
	startMQTT()
	while True:
		time.sleep(2)

if __name__ == "__main__":
	main()
