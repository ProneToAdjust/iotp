import time
import paho.mqtt.client as mqtt
import psutil

mqtt_broker = "m2m.eclipse.org"
topic = "tp/eng/iotp_lab/pc_010101/cpu"
topic2 = "tp/eng/iotp_lab/pc_010101/virtual_mem"

while True:
	cpu_usage = psutil.cpu_percent(interval=10)
	pay_load = "CPU_Usage="+str(cpu_usage)
	
	vir_mem = psutil.virtual_memory()
	pay_load2 = "Vir_mem="+str(vir_mem.available)
	
	my_mqtt = mqtt.Client()
	print("\nCreated client object at "+ time.strftime("%H:%M:%S"))
	
	my_mqtt.connect(mqtt_broker, port=1883)
	print("--connected to broker")
	
	try:
		my_mqtt.publish(topic, pay_load)
		print("--cpu usage percent = %.1f" % cpu_usage)
		
		my_mqtt.publish(topic2, pay_load2)
		print(vir_mem.available)
		
	except:
		print("--error publishing!")
		
	else:
		my_mqtt.disconnect()
		print("--disconnected from broker")