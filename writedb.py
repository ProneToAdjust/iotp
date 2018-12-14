import argparse
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import time
import random
USER = 'root'
PASSWORD = 'root'
DBNAME = 'mydb'
HOST = 'localhost'
PORT = 8086
dbclient = None;

def main():
	dbclient = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)
	while True:
		data_point = getSensorData()
		dbclient.write_points(data_point)
		print("Written data")
		time.sleep(2)

def getSensorData():
	sensorData = random.randint(15, 40)
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

if __name__ == '__main__':
	main()