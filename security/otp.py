#!/usr/bin/python

import sys
import os
import smtplib
from twilio.rest import TwilioRestClient
from random import randint
import getpass

user= getpass.getuser()

otpa=(randint(1000,99999))
print otpa
def clientIp():
	sshvalue=os.environ["SSH_CLIENT"]
	ip=str.split(sshvalue)
	print ip[0]

def Sms():
	ACCOUNT_SID = "AC*****************************"
	AUTH_TOKEN = "64******************************"
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	
	client.messages.create(
		to="+91*********", # provide the number in you want to get otp
		from_="+*******",
		body="otp = "+ str(otp) +" for ip" + ip[0],
	
		#media_url="https://climacons.herokuapp.com/clear.png",
		)
Sms()
def mail():
	msg = "\r\n".join([
	"From: *****@***.com",
	"To: annadpratik141@gmail.com",
	"Subject: OTP for ssh login",
	"",
	"User name: " + user, 
	"otp: " + str(otpa),
	"ip: " + str(ip[0])
	
	])
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() 
	server_ssl.login("user name", "Password")
	server_ssl.sendmail("*****", "******" , msg)
	server_ssl.close()
	print "mail Send :)"


def otp():
	try:
		a= raw_input("Enter the otp: ")
		print a
		# test
	except KeyboardInterrupt:
		print "Not Allowed"
		otp()
otp()
mail()
