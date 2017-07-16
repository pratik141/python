#!/usr/bin/python

"""
  Author name : Pratik Anand
  Authon Email: pratik.anand@mobiliya.com
  Description : Teams notification Service
"""

from termcolor import colored ,cprint  ## for colored output
import yaml as yml
import getpass
import sys
import os

configFile = "config.yml"
tmpdic     = {}
appdata    = {}

print(colored("   Enter 'ooo' or 'OOO' for exit \n \
  'reconf' for reconfigure ", 'magenta' ,attrs=['bold']))

def warn(val):
  print(colored( "%s" %(val), 'yellow'))

def error(val):
  print(colored( "%s" %(val), 'red', attrs=['bold']))
  exit()

def info(val):
  print(colored( "%s" %(val), 'cyan'))

def question(val):
  cprint( "%s" %(val), 'magenta', end=' ')


def takeInput(msg,required):
  question(msg)
  if sys.version_info[0] < 3:
    ans = raw_input()
  else:
    ans = input()

  if not ans:
      warn("You entered nothing...!")
      return takeInput(msg,required)

    ###  Exit keyword ###
  elif ans in ['ooo', 'OOO']:
    error("Closing instance.")

  elif ans in ['reconf', 'RECONF']:
    warn("Removing config file")
    import os
    try:
      os.remove((os.path.dirname(os.path.realpath(__file__)))+'/config.yml')
    except OSError as e:
      warn(e)
    return takeInput(msg,required)

  else:

    if ans.isdigit():
      current = 'int'
    elif set('[~!@#$%^&*()_+{}":/\']+$').intersection(ans):
      current = 'other'
    elif sys.version_info[0] > 3 and isinstance(ans,basestring):
      current = 'str'
    elif sys.version_info[0] < 3 or isinstance(ans,str): ## python 3
      current = 'str'
    else:
      current = 'none'

  if required == current :
    return ans
  else:
    if 'required' in  msg :
      return takeInput(msg,required)
    else:
      return takeInput(msg+'(required: %s)' %required,required)


################################


def getInput(appname):
  if appname is 'teams':
    appdata['URL'] = takeInput('Enter the URL','str')

  elif appname in ['outlook_mail','gmail_mail']:
    appdata['emailId'] = takeInput('Enter the email Id','str')
    question('Enter the email password')
    appdata['emailPassword'] = getpass.getpass()

  elif appname in ['twilio_sms']:
    appdata['sid'] = takeInput('Enter the ACCOUNT_SID:','str')
    appdata['sender'] = takeInput('Enter the sender:','str')
    question('Enter the AUTH_TOKEN')
    appdata['token'] = getpass.getpass()

  return appdata

def createConfig(appname,datadic):
  if appname is 'teams':
    info("""
    To get URL for your Teams channels please follow bellow steps:-
      1.) Login to your Teams accounts "https://teams.microsoft.com/".
      2.) Click on more option in teams channels and select connector.
      3.) Search webhook and click on add button of Incoming Webhook.
      4.) Write a name in the box and click on Create button.
      5.) Copy the generated link and paste it here.
   """ )

  datadic[appname] = getInput(appname)
  try:
    f = open(configFile, 'w')
    f.write(yml.dump(datadic, indent=2 ,
            default_flow_style=False,
            Dumper=yml.SafeDumper,
            explicit_start=True))
    f.close()
    return datadic[appname]
  except Exception as e:
    os.remove('config.yml')
    print (e)

def readConfig(appname):
  if os.path.isfile(configFile):

    try:
      f = open(configFile, "r")
      data = yml.load(f)
      f.close()
      if data.get(appname) == None:
        return createConfig(appname,data)
      return data.get(appname)

    except Exception as e:
      f = open(configFile, "r")
      data = yml.load(f)
      f.close()

      if data == None:
        data = {}
      return createConfig(appname,data)

  else:
    print (configFile , "Not avail")
    return createConfig(appname,datadic={})


def reConfig(appname):

  f = open(configFile, "r")
  data = yml.load(f)
  f.close()
  if data == None:
    data = {}
  return createConfig(appname,data)
