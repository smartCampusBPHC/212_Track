import flask
from collections import deque
from flask import Flask,request ,render_template
import os
import datetime
import time
import json

# 212 tracking API Key AIzaSyBW33L4Qzpx6nAzfa5DOFd1T-uChYxjHyE

dataPoints = deque()

def time_min(sec):
	return datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
	if request.method=='GET':
		return render_template('map.html',dataPoints=dataPoints,dataPointsJson=json.dumps(dataPoints))
		
@app.route("/data", methods=['GET','POST'])
def data():	
	if request.method=='GET':

		# data = request.get_json(force=True)
		# print data
		id_bus = request.args.get('uid')
		print id_bus
		lati = float(request.args.get('latitude'))
		print lati
		longi = float(request.args.get('longitude'))
		print longi
		time = int(request.args.get('time'))
		time = time_min(time)
		print time
	
		if (id_bus and lati and longi and time):
			dataPoints.append((id_bus,lati,longi,time))
			if len(dataPoints) > 3:
				dataPoints.popleft()
			print dataPoints

		return ("recieved data")
		
		

port = int(os.getenv('VCAP_APP_PORT', 8080))
if __name__=='__main__':
	app.run(host='0.0.0.0', port=port, debug=True)