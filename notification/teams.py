#!/usr/bin/python


"""
  Author name : Pratik Anand
  Authon Email: pratik.anand@mobiliya.com
  Description : Teams notification Service
"""

import commonService as cs
import requests
import base64
import json

url     = cs.readConfig('teams')
headers = {'content-type': 'application/json'}  ## Comman for all

def send(Title,Message,Remarks='none'):

  payload='''
  {
    "title": "%s",
    "text": "Message => %s",
    "themeColor": "%s"

  }'''%(Title,Message,'00ea43')
  print (url, payload, headers)
  try:
    req = requests.post(url, payload, headers)
  except:
    req = requests.post(url, payload)

  return  "Status Code: " %(req.status_code)
