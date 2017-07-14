#!/usr/bin/env python

import commonService as cs
try:
  from O365 import Message, Attachment
except Exception as e:
  cs.error('please install O365 module \"sudo pip install O365\" ')


def creteHtmlMsg(subject):

### converting msg into html format  ###

  htmlMsg = """

<h4> Hi All,</h4>
  <p>

 <br>
<br> This is test mail.:)<br>
    PFA
  <br><br>
With Regards, <br>
&nbsp; Pratik Anand
    </p>

    """

  msg=str(htmlMsg)
  return msg

def SendMail(sender,msg,subject,filenmame=None):

  outlook_config_data = cs.readConfig('outlook_mail')
  emailId  = outlook_config_data.get('emailId')
  password = outlook_config_data.get('emailPassword')

  if emailId == None or password == None:
    cs.warn('unable to retrive mail cred')
    cs.reConfig('outlook_mail')
    return SendMail(sender,msg,subject,filenmame)

  authenticiation =(emailId,password)
  m = Message(auth=authenticiation)
  m.setRecipients(sender)
  m.setSubject(subject)
  m.setBodyHTML(msg)
  m.setSenderName()

  if filenmame:
    att = Attachment(path=filenmame)
    m.attachments.append(att)

  mailSendStatus = m.sendMessage()

  return mailSendStatus


# downloadFile = ('/tmp/test.txt')
# sender = ["pratik.anand@mobiliya.com", "anandpratik141@gmail.com"]
# subject = "Test Mail"
# msg = creteHtmlMsg(subject)
# SendMail('sender','msg','subject','downloadFile')
