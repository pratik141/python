#!/usr/bin/python

import sys
import smtplib
from twilio.rest import TwilioRestClient
from termcolor import colored
from random import randint
import getpass

user= getpass.getuser()
i = 1

otp=(randint(1000,99999))
print otp
def clientIp():
	global ip
	sshvalue=os.environ["SSH_CLIENT"]
	ip=str.split(sshvalue)
	print ip[0]

def Sms():
	global ip
	ACCOUNT_SID = "AC*****************************"
	AUTH_TOKEN = "64******************************"
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	
	client.messages.create(
		to="+91*********", # provide the number in you want to get otp
		from_="+*******",
		body="otp = "+ str(otp) +" for ip" + ip[0],
	
		#media_url="https://climacons.herokuapp.com/clear.png",
		)

def mail():
	global ip
	msg = "\r\n".join([
	"From: *****@***.com",
	"To: annadpratik141@gmail.com",
	"Subject: OTP for ssh login",
	"",
	"User name: " + user, 
	"otp: " + str(otp),
	"ip: " + str(ip[0])
	
	])
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() 
	server_ssl.login("user name", "Password")
	server_ssl.sendmail("*****", "******" , msg)
	server_ssl.close()
	print "mail Send :)"


def otpFun():
	global i
	global otp
	try:
		try:
			i = i + 1 
			pin= raw_input("Enter the otp: ")
			if otp == int(pin):
				print "Welcome to ", user ,"system"
			else:
				if i == 3:
					print colored(' You have last attempt', 'red')
				if i == 4:
					sys.exit(0)
				print "Wronge Pin"
				otpFun()
		except Exception, e:
			print e
	except KeyboardInterrupt:
		print "Not Allowed"
		otpFun()

### calling function
Sms()
mail()
otpFun()