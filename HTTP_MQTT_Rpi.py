#importing the important libraries.
import RPi.GPIO as GPIO
from Adafruit_IO import MQTTClient
import sys

import urllib.request as u
api="https://api.thingspeak.com/update?api_key=MHRGX65CYK624MA5&field1="
api2="https://api.thingspeak.com/update?api_key=MHRGX65CYK624MA5&field2="
#setting GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pin Number of the pi to which we are connecting our bulbs
BULB1 = 20
BULB2 = 21

#setting the pin no. as output
GPIO.setup(BULB1, GPIO.OUT)
GPIO.setup(BULB2, GPIO.OUT)

#adding adafruit_io key and username
ADAFRUIT_IO_KEY = 'aio_yEkv13A6q4hy3ZfMJ9mwjjO6wMbP'
ADAFRUIT_IO_USERNAME = 'amritraj1544'

#adding feed name of the button we are using from the adafruit
Feed_id1 = 'bulb1'
Feed_id2 = 'bulb2'

#defining function for connecting the bulbs to the adafruit_io
def connected_to_adafruit(client):
    print('Connecting to {0}'.format(Feed_id1))
    client.subscribe(Feed_id1)
    print('Connecting to {0}'.format(Feed_id2))
    client.subscribe(Feed_id2)
    print('Waiting for your command...')
        
def disconnected_from_adafruit(client):
    sys.exit(1)
    
#defining function for receiving the message from the user's app   
def message_from_user(client, Feed_id, payload):
    if Feed_id=="bulb1":
        if payload == "1":
           print('BULB1 is ON')
           GPIO.output(BULB1, GPIO.HIGH)
           a=u.urlopen(api+str(1))
        else:
           print('BULB1 is OFF')
           GPIO.output(BULB1, GPIO.LOW)
           a=u.urlopen(api+str(0))
    if Feed_id=="bulb2":
        if payload == "1":
           print('BULB2 is ON')
           GPIO.output(BULB2, GPIO.HIGH)
           a=u.urlopen(api2+str(1))
        else:
           print('BULB2 is OFF')
           GPIO.output(BULB2, GPIO.LOW)
           a=u.urlopen(api2+str(0))
          
           
#Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#Setup the callback functions defined above.
client.on_connect = connected_to_adafruit
client.on_disconnect = disconnected_from_adafruit
client.on_message = message_from_user

#Connect to the Adafruit IO server.
client.connect()
client.loop_blocking()
