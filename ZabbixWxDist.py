#!/usr/bin/env python3

import requests
import json
import sys
import time
import random
import os.path

if len(sys.argv) != 4:
    print("Expected 3 arguments", file=sys.stderr)
    sys.exit(1)

apikey = sys.argv[2]
appkey = sys.argv[3]

wxDataFile = "/tmp/wxData.json"
url = "https://api.ambientweather.net/v1/devices?applicationKey="+ appkey +"&apiKey=" + apikey

if os.path.exists(wxDataFile) and (time.time() - os.path.getmtime(wxDataFile) < 20):
    with open(wxDataFile) as json_file:
        wxData = json.load(json_file)
else:
    response = requests.request("GET", url)
    if response.status_code == 200:
        wxData = response.json()
        with open(wxDataFile, 'w') as outfile:
            json.dump(wxData, outfile)
    else:
        print(response.text, file=sys.stderr)
        sys.exit(1)

try:
    OutputWx = float(wxData[0]['lastData'][sys.argv[1]])
except (KeyError,ValueError) as e:
    print("Invalid data in response", file=sys.stderr)
    sys.exit(1)

print(OutputWx)
