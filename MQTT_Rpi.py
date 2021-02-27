import RPi.GPIO as GPIO
import sys
from Adafruit_IO import MQTTClient
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 20
ledpin2 = 21
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(ledpin2, GPIO.OUT)
ADAFRUIT_IO_KEY = ''
ADAFRUIT_IO_USERNAME = ''
Feed_id1 = 'bulb1'
Feed_id2 = 'bulb2'
def connected(client):
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(Feed_id1))
    client.subscribe(Feed_id1)
    print('Subscribing to Feed {0}'.format(Feed_id2))
    client.subscribe(Feed_id2)
    print('Waiting for feed data...')
def disconnected(client) :
    sys.exit(1)
def message1(client, Feed_id, payload1):
    if Feed_id=="bulb1":
        print('Feed {0} received new value: {1}'.format(Feed_id, payload1))
        if payload1 == "1":
           GPIO.output(ledPin, GPIO.HIGH)
        else:
           GPIO.output(ledPin, GPIO.LOW)
    if Feed_id=="bulb2":
        print('Feed {0} received new value: {1}'.format(Feed_id2, payload1))
        if payload1 == "1":
           GPIO.output(ledpin2, GPIO.HIGH)
        else:
           GPIO.output(ledpin2, GPIO.LOW)
#Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message1
#client.on_message = message1
#Connect to the Adafruit IO server.
client.connect()
client.loop_blocking()
