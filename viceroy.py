import flask
from collections import deque
from flask import Flask,request ,render_template
import os
import datetime
import time
import json

# 212 tracking API Key AIzaSyBW33L4Qzpx6nAzfa5DOFd1T-uChYxjHyE

dataPoints = deque()
dataPointsById = {} #id: deque
dataPointsToMap = {} #id: list, passed to map.html
arr = []

def time_min(sec):
	return datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
	if request.method=='GET':
		print "here"
		print "\n\n",dataPointsToMap,"\n",json.dumps(dataPointsToMap)
		return render_template('map.html',dataPoints=str(json.dumps(dataPointsToMap)))

@app.route("/data", methods=['GET','POST'])
def data():	
	if request.method=='POST':

		# data = request.get_json(force=True)
		# print data
		id_bus = request.args.get('uid')

		id_bus2 = request.json['uid']
		#return id_bus2
		#return "Bus ID: "+ str(id_bus2)
		#lati = float(request.args.get('latitude'))
		#print "Latitude: ",lati
		lati = str(request.json['latitude'])
		longi = str(request.json['longitude'])
		time = str(request.json['time'])
		arr.append(lati)
		arr.append(longi)
		arr.append(time)
		#return arr[1]
		#return str(lati)
		#longi = float(request.args.get('longitude'))
		#print "Longitude: ",longi
		#time = int(request.args.get('time'))
		#time = time_min(time)
		#print "Time: ",time
		
		#lati,longi,time goes to resp. id_bus deque
		if (id_bus2 and lati and longi and time):
			if id_bus2 not in dataPointsById:
				dataPointsById[id_bus2] = deque()
			dataPointsById[id_bus2] = ((lati,longi,time))

			if len(dataPointsById[id_bus2]) > 3:
				dataPointsById[id_bus2].popleft()
			print "dataPointsById:\n",id_bus2,"-",dataPointsById[id_bus2]
			print "heehee"

			dataPointsToMap[id_bus2] = list(dataPointsById[id_bus2])
			print "dataPointsToMap:\n",id_bus2,"-",dataPointsToMap[id_bus2]

		else:
			# data = request.get_json(force=True)
			# print data
			id_bus = request.args.get('uid')
			
			#id_bus2 = request.json['uid']
			#return id_bus2
			#return "Bus ID: "+ str(id_bus2)
			lati = float(request.args.get('latitude'))
			print "Latitude: ",lati
			#lati = str(request.json['latitude'])
			#longi = str(request.json['longitude'])
			#time = str(request.json['time'])
			#arr.append(lati)
			#arr.append(longi)
			#arr.append(time)
			#return arr[1]
			#return str(lati)
			longi = float(request.args.get('longitude'))
			print "Longitude: ",longi
			time = int(request.args.get('time'))
			time = time_min(time)
			print "Time: ",time
			
			#lati,longi,time goes to resp. id_bus deque
			if (id_bus and lati and longi and time):
				if id_bus not in dataPointsById:
					dataPointsById[id_bus] = deque()
				dataPointsById[id_bus] = ((lati,longi,time))

				if len(dataPointsById[id_bus]) > 3:
					dataPointsById[id_bus].popleft()
				print "dataPointsById:\n",id_bus,"-",dataPointsById[id_bus]
				print "heehee"

				dataPointsToMap[id_bus] = list(dataPointsById[id_bus])
				print "dataPointsToMap:\n",id_bus,"-",dataPointsToMap[id_bus]

		return ("recieved datas")
		

port = int(os.getenv('VCAP_APP_PORT', 5000))
if __name__=='__main__':
	app.run(host='127.0.0.1', port=port, debug=True)