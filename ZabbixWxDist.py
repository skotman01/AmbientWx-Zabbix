#!/usr/bin/python3.6m

import requests
import json
import sys
from decimal import *
import time
import random 
import os.path
from os import path

apikey = sys.argv[2]
appkey = sys.argv[3]

wxDataFile = "/tmp/wxData.json"
url = "https://api.ambientweather.net/v1/devices?applicationKey="+ appkey +"&apiKey=" + apikey

if path.exists(wxDataFile):
    if time.time() - path.getmtime(wxDataFile) < 20:
        with open(wxDataFile) as json_file:
            wxData = json.load(json_file)
    else:
        response = requests.request("GET", url)
        jsonData = response.text.encode('utf8')
        wxData = json.loads(jsonData)
        with open(wxDataFile, 'w') as outfile:
            json.dump(wxData, outfile)
else:
    response = requests.request("GET", url)
    jsonData = response.text.encode('utf8')
    wxData = json.loads(jsonData)
    with open(wxDataFile, 'w') as outfile:
        json.dump(wxData, outfile)

OutputWx = Decimal(wxData[0]['lastData'][sys.argv[1]])

print(OutputWx)
