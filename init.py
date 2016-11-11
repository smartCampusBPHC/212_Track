#pin on center
import json
import requests

url = 'http://212track.mybluemix.net'
# url = 'http://localhost:8080'
headers = {'Content-Type': 'application/json'}
payload = {'latitude': 17.4977899, 'id': 'ajfnsajnfjnjlnlfnsakf', 'longitude': 78.5056246}

payload = json.dumps(payload)
print payload

for i in range(3):
	r = requests.get (url , headers = headers ,data=payload)
	print r.status_code
