#!/usr/bin/env python

"""
  Author name : Pratik Anand
  Authon Email: anandpratik141@gmail.com
  Description : SMS notification Service via twilio using twilio rest lib

"""

import commonService as cs
try:
  from twilio.rest import Client as twilio_cli
except Exception as e:
  cs.error('please install twilio module \"sudo pip install twilio\" ')

def SendSms(msg):

  twilio_config_data = cs.readConfig('twilio_sms')
  ACCOUNT_SID = twilio_config_data.get('sid')
  AUTH_TOKEN  = twilio_config_data.get('token')
  sender      = twilio_config_data.get('sender')

  client = twilio_cli(ACCOUNT_SID, AUTH_TOKEN)

  client.messages.create(
          to="+91*********", # provide the number
          from_=sender,
          body=msg,
          #media_url="https://climacons.herokuapp.com/clear.png",
          )
  return "Msg sent"
