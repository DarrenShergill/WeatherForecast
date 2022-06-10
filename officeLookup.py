#!/usr/bin/env
import json
import urllib.request
#lat='36.585'
#long='-119.624'
lat='37.518'
long='-121.92'
parsed = ""
PRequest='https://api.weather.gov/points/' + lat + ',' + long
with urllib.request.urlopen(PRequest) as response:
   html = response.read()
   parsed = json.loads(html)['properties']['forecast']
   print(json.dumps(parsed, indent=4, sort_keys=True))


PRequest = parsed
with urllib.request.urlopen(PRequest) as response:
   html = response.read()
   periods = json.loads(html)['properties']['periods']
   #for period in periods:
       #print(period['startTime'],period['temperature'])
   print(json.dumps(periods, indent=4, sort_keys=True))

"https://api.weather.gov/gridpoints/MTR/100,90/forecast"