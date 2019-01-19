import time
import json
import paho.mqtt.client as mqtt

mqtt_broker = "m2m.eclipse.org"
topic_cpu = "iotp/tph"
my_mqtt = None

def onMessage(client, userdata, message):
	m_decode=str(message.payload.decode("utf-8","ignore"))
	f = open("var.txt","w")
	f.write(m_decode)
	f.close()
	print(m_decode)

def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic_cpu, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to topic")
	
def main():
	startMQTT()
	while True:
		time.sleep(2)

if __name__ == "__main__":
	main()