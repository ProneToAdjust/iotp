import time
import paho.mqtt.client as mqtt
import psutil
mqtt_broker = "m2m.eclipse.org"
topic_cpu = "tp/eng/iotp_lab/pc_010101/cpu"
topic_vmem = "tp/eng/iotp_lab/pc_010101/virtual_mem"
my_mqtt = None
def onMessage(client, userdata, message):
	print("%s %s" % (message.topic, message.payload))

def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic_cpu, qos=1)
	my_mqtt.subscribe(topic_vmem, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to topic1")
	
	#my_mqtt = mqtt.Client()
	#my_mqtt.on_message = onMessage
	#my_mqtt.connect(mqtt_broker, port=1883)
	#my_mqtt.subscribe(topic_vmem, qos=1)
	#my_mqtt.loop_start()
	print("Subscribed to topic2")

def main():
	startMQTT()
	while True:
		time.sleep(2)

if __name__ == "__main__":
	main()