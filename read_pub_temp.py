# import necessary packages
import smbus2
import bme280
import time
import paho.mqtt.client as mqtt
import json

# initialise mqtt broker and topic to be used
mqtt_broker = "m2m.eclipse.org"
topic = "iotp/tph"

# initialise calibration parameters for reading bme280
port = 1
address = 0x76
bus = smbus2.SMBus(port)

# initialise list for temperature, pressure and humidity
tph = [None, None, None]

# load calibration parameters to bme280
calibration_params = bme280.load_calibration_params(bus, address)

# start loop
while True:

    # read data from bme280
    data = bme280.sample(bus, address, calibration_params)

    # load data read into list
    tph[0] = data.temperature
    tph[1] = data.pressure
    tph[2] = data.humidity

    # convert list to json
    payload = json.dumps(tph)

    # start mqtt client
    my_mqtt = mqtt.Client()
    print("\nCreated client object at " + time.strftime("%H:%M:%S"))

    # connect mqtt client to broker
    my_mqtt.connect(mqtt_broker, port=1883)
    print("--connected to broker")

    # try catch block to publish message to broker
    try:
        # publish message to broker
        my_mqtt.publish(topic, payload)
        print(payload)

        time.sleep(1)

    except:
        print("--error publishing!")

    else:
        # disconnect on message publish success
        my_mqtt.disconnect()
        print("--disconnected from broker")
