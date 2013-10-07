import socket
import time
import ssl
import datetime
import random
import re

# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "channel.example.com" # Server to connect to
HOME_CHANNEL = "#channel" # The home channel for your bot
NICK = "ChatBot" # Your bots nick
PORT = 6667 # Port (it is normally 6667)
SYMBOL = "#" #symbol eg. if set to # commands will be #echo.
PASSWORD = "password" # password to the room
blank = ""
###########################
##plugin loading varibles##
###########################
food = True
email = True

def ping(msg):
  ircsock.send("PONG :"+ msg +"\r\n")
def joinchan(channel):
  ircsock.send("PRIVMSG "+ CHANNEL +" :Joining "+ channel +"\r\n")
  ircsock.send("JOIN "+ channel +"\r\n")
def partchan(channel):
  ircsock.send("PRIVMSG "+ CHANNEL +" :Leaving "+ channel +"\r\n")
  ircsock.send("PART "+ channel +"\r\n")
def hello(user):
  ircsock.send("PRIVMSG "+ CHANNEL +" :G'day "+ user +"!\n")
def quitIRC(): #if somebody quits the Chatbot it will email the admin
  if email == True:
    me = "from@email.com" #the sender's email address
    family = "to@eamil.com" #enter the recipients email here
    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'Chat Bot is Down'
    msg['From'] = me
    msg['To'] = family
    msg.preamble = 'Test'
    text = "Chatbot has been shut down\n"
    date = datetime.datetime.now()
    text2 = date.strftime("%Y-%m-%d %H:%M")
    
    #if you want html in the mesage follow the format below.
  #  html = """\
  #  <html>
  #    <head></head>
  #    <body>
  #      <p>Hi!<br>
  #        How are you?<br>
  #        Here is the <a href="http://www.python.org">link</a> you wanted.
  #      </p>
  #    </body>
  #  </html>
  #  """
  
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    #part2 = MIMEText(html, 'html')
    part3 = MIMEText(text2, 'plain')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    #msg.attach(part2)
    msg.attach(part3)

    # Send the email via our own SMTP server.
    a = smtplib.SMTP('localhost')
    a.sendmail(me, family, msg.as_string())
    a.quit()

  ircsock.send("QUIT "+ CHANNEL +"\n")
def kickme(target, reason):
  ircsock.send("KICK "+ CHANNEL +" "+ target +" "+ reason + "\n")
def fail():
  ircsock.send("PRIVMSG "+ CHANNEL +" :Either you do not have the permission to do that, or that is not a valid command.\n")
def fish(user):
  ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION slaps "+ user +" with a wet sloppy tuna fish.\x01\r\n")
  time.sleep(1)
  ircsock.send("PRIVMSG "+ CHANNEL +" :take that bitch\n")
def sandwich(sender):
  if food == True:
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION is making "+ sender +" a sandwich\x01\r\n")
     time.sleep(10)
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION has finished making "+ sender +"'s sandwhich\x01\r\n")
     time.sleep(1)
     ircsock.send("PRIVMSG "+ CHANNEL +" :Here you go "+ sender +"! I hope you enjoy it!\r\n")
  else:
     ircsock.send("PRIVMSG "+ CHANNEL +" :Command not loaded\r\n")
def makeitem(nick, item):
  ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION is making "+ nick +" a "+ item +"\x01\r\n")
  time.sleep(10)
  ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION has finished making "+ nick +"'s "+ item +"\x01\r\n")
  time.sleep(1)
  ircsock.send("PRIVMSG "+ CHANNEL +" :Here you go "+ nick +"! I hope you enjoy it!\r\n")
def bomb(user):
  ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION hurls a bomb in "+ user +"'s direction.\x01\r\n")
  time.sleep(0.5)
  ircsock.send("PRIVMSG "+ CHANNEL +" :BOOM!\n")
  ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION bomb explodeircsock.\x01\r\n")
  ircsock.send("KICK ##aussiepowder "+ user +" Bombed\n")
  time.sleep(1.75)
  ircsock.send("PRIVMSG "+ CHANNEL +" :and you thought you could take on a bot with such awesomeness! pfft\n")

def timesheets(times):
  if food == True:
    for x in range(0, times):
      ircsock.send("PRIVMSG "+ CHANNEL +" :Do your timesheets everyone!\n")
      time.sleep(4)
  else:
    ircsock.send("PRIVMSG "+ CHANNEL +" :Command not loaded\r\n")

def cake(sender):
   if food == True: 
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION is making "+ sender +" a cake\x01\r\n")
     time.sleep(10)
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION has finished making "+ sender +"'s cake\x01\r\n")
     time.sleep(1)
     ircsock.send("PRIVMSG "+ CHANNEL +" :Here you go "+ sender +"! I hope you enjoy it!\r\n")
     time.sleep(20)
     ircsock.send("PRIVMSG "+ CHANNEL +" :The cake is NOT a lie!\r\n")
     time.sleep(1)
     ircsock.send("PRIVMSG "+ CHANNEL +" :Really, it isn't\r\n")
   else:
     ircsock.send("PRIVMSG "+ CHANNEL +" :Command not loaded\r\n")
def echo(message):
  ircsock.send("PRIVMSG "+ CHANNEL +" :"+ message +"\r\n") 
def pepsi(user):
  if food == True:
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION dispenses a can of Pepsi for "+ user +"\x01\r\n")
  else:
     ircsock.send("PRIVMSG "+ CHANNEL +" :Command not loaded\r\n")
def coke(user):
  if food == True:
     ircsock.send("PRIVMSG "+ CHANNEL +" :\x01ACTION dispenses a can of Coke for "+ user +"\x01\r\n")
  else:
     ircsock.send("PRIVMSG "+ CHANNEL +" :Command not loaded\r\n")
def load(plugin):
  if plugin =="food":
     global food
     food = True
     ircsock.send("PRIVMSG "+ CHANNEL +" :LOADED the FOOD plugin\r\n")
  else:
      ircsock.send("PRIVMSG "+ CHANNEL +" :UNKNOWN plugin\r\n")
     
def unload(plugin):
  if plugin =="food":
     global food
     food = False
     ircsock.send("PRIVMSG "+ CHANNEL +" :UNLOADED the FOOD plugin\r\n")
  else:
     ircsock.send("PRIVMSG "+ CHANNEL +" :UNKNOWN plugin\r\n")

def roll(times, die):
  total = ""
  if food == True:
    for x in range(0, times):
      number =  int((random.random() * die) + 1)
      total += "" + str(number) + " "
    ircsock.send("PRIVMSG "+ CHANNEL +" :" + total + "\r\n")
  else:
    ircsock.send("PRIVMSG "+ CHANNEL +" :UNKNOWN plugin\r\n")

def help():
  if food == True:
    ircsock.send("PRIVMSG "+ CHANNEL +" :Usage examples:  #roll <number>d<number> ex: '1d6', #pepsi <number>, #coke <number>, #bomb <nick>, #fish, #cake, #echo <String>, #timesheets <number>\r\n")
  else:
    ircsock.send("PRIVMSG "+ CHANNEL +" :UNKNOWN plugin\r\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
ircsock = ssl.wrap_socket(s)
ircsock.send("PASS " + PASSWORD + "\n")
ircsock.send("USER "+ NICK +" "+ NICK +" "+ NICK +" :my awsomebot\n")
ircsock.send("NICK "+ NICK +"\r\n")
ircsock.send("JOIN "+ HOME_CHANNEL +"\n")

while 1:
  line = ircsock.recv(2048)
  line = line.strip('\r\n')
  print line
  stoperror = line.split(" ")
  if ("PING :" in line):
        pingcmd = line.split(":", 1)
        pingmsg = pingcmd[1]
        ping(pingmsg)
  elif "PRIVMSG" in line:
      
      if len(line) < 30:
        print blank
      elif len(stoperror) < 4:
        print blank
      else:
        complete = line.split(":", 2)
        info = complete[1]
        msg = line.split(":", 2)[2] ##the thing that was said
        cmd = msg.split(" ")[0]
        CHANNEL = info.split(" ")[2] ##channel from which it was said
        user = line.split(":")[1].split("!")[0] ## the person that said the thing
        arg = msg.split(" ")
        
        if msg.find("hello "+ NICK) != -1:
          hello(user)
          print "recieved hello"
        elif msg.find("hey "+ NICK) != -1:
          hello(user)
          "print recieved hello"
        elif msg.find("hi "+ NICK) != -1:
          hello(user)
          "print recieved hello"
        elif SYMBOL + "join"==cmd and len(arg) > 1:
          x = line.split(" ", 4)
          newchannel = x[4]
          joinchan(newchannel)
        elif SYMBOL + "leave"==cmd and len(arg) > 1:
          x = line.split(" ", 4)
          newchannel = x[4]
          partchan(newchannel)
        elif SYMBOL + "quit"==cmd:
          quitIRC()
          break
        elif SYMBOL + "coke"==cmd and len(arg) > 1:
          x = line.split(" ")
          recvr = x[4]
          coke(recvr)
        elif SYMBOL + "pepsi"==cmd and len(arg) > 1:
          x = line.split(" ")
          recvr = x[4]
          pepsi(recvr)
        elif SYMBOL + "fish"==cmd and len(arg) > 1:
          x = line.split(" ")
          recvr = x[4]
          fish(recvr)
        elif SYMBOL + "bomb"==cmd and len(arg) > 1:
          x = line.split(" ")
          recvr = x[4]
          bomb(recvr)
        
        elif SYMBOL + "timesheets"==cmd and len(arg) > 1:
          x = line.split(" ")
          recvr = int(x[4])
          timesheets(recvr)
        
        elif SYMBOL + "roll"==cmd and len(arg) > 1:
          x = line.split(" ")
          y = re.split("([d|D])", x[4])
          if len(y[0]) > 1:
            ircsock.send("PRIVMSG "+ CHANNEL +" :Invalid Input!\r\n")
          else:
            roll(int(y[0]), int(y[2]))

        elif SYMBOL + "fish"==cmd:
          sandwich(user)
        elif SYMBOL + "cake"==cmd:
          cake(user)
        elif SYMBOL + "echo"==cmd:
          x = msg.split(" ", 1)[1]
          echo(x)

        elif SYMBOL + "help"==cmd:
          help()

        elif line.find(""+ SYMBOL +"load") != -1:
          plugin = msg.split(" ")[1]
          load(plugin)
       
        elif line.find(""+ SYMBOL +"unload") != -1:
          plugin = msg.split(" ")[1]
          unload(plugin)
       
        elif SYMBOL in cmd:
          fail()
