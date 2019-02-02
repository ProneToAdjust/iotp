# import necessary packages
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import time
import json
import paho.mqtt.client as mqtt

# initialise parameters for database access
USER = 'root'
PASSWORD = 'root'
DBNAME = 'mydb'
HOST = 'localhost'
PORT = 8086
dbclient = None

# initialise mqtt broker and topic to be used
mqtt_broker = "m2m.eclipse.org"
topic = "iotp/tph"
my_mqtt = None

# initialise sensor data
sensorData = 0


def main():
    # create influx db client class
    dbclient = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)

    # run function to start mqtt subscriber
    startMQTT()

    # start loop
    while True:

        if sensorData:
            # get data points with sensor data
            data_point = getSensorData()

            # write data points into db
            dbclient.write_points(data_point)
            print(data_point)
            print("Written data")
            time.sleep(2)
        continue


def getSensorData():
    # get current time
    now = time.gmtime()

    # create point values with sensor data
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

    return pointValues


def onMessage(client, userdata, message):
    global sensorData

    # convert json back to list
    m_decode=str(message.payload.decode("utf-8","ignore"))
    tph = json.loads(m_decode)

    # set temperature as sensor data
    sensorData = tph[0]


# function to initialise mqtt subscriber client
def startMQTT():
    my_mqtt = mqtt.Client()
    my_mqtt.on_message = onMessage
    my_mqtt.connect(mqtt_broker, port=1883)
    my_mqtt.subscribe(topic, qos=1)
    my_mqtt.loop_start()
    print("Subscribed to topic")


if __name__ == '__main__':
    main()
