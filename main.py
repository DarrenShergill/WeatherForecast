#!/usr/bin/env
import json
import urllib.request
import os


latitude = os.getenv('LAT')
longitude = os.getenv('LONG')
office = os.getenv('OFFICE')
grid = os.getenv('GRID')
print(office)
print(grid)

def lat_and_long(lat,long):
   forecasturl = ""
   points= f"https://api.weather.gov/points/{lat}' + ',' + {long}"
   with urllib.request.urlopen(points) as response:
      html = response.read()
      forecasturl = json.loads(html)['properties']['forecast']
   parse_report(forecasturl)

def office_and_grid(o,g):
   grid_URL = f"https://api.weather.gov/gridpoints/{o}/{g}/forecast"
   parse_report(grid_URL)

def parse_report(url):
   with urllib.request.urlopen(url) as response:
      html = response.read()
      periods = json.loads(html)['properties']['periods']
      print(json.dumps(periods, indent=4, sort_keys=True))

if office and grid:
   office_and_grid(office,grid)
elif latitude and longitude:
   lat_and_long(latitude,longitude)
else:
   print("BIG ERROR")







