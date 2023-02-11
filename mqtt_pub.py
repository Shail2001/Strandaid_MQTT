import time
import paho.mqtt.client as mqtt
from random import seed
from random import randint

broker_address = "192.168.0.101"

client1 = mqtt.Client("PUB1")
client1.connect(broker_address)

wbat = 100
direction = ["Moved to Left Side", "Moved to Right Side", "Elevation", "Decline"]
objdet = "Object Detected!!"
signal = "Signal Received!"

while True:
    client1.publish('comm/msg1', wbat)
    wbat -= 0.25
    time.sleep(3)
    indexValue = randint(0,3)
    movement = direction[indexValue]
    client1.publish('comm/msg2', movement)
    time.sleep(3)
    client1.publish('comm/msg3', objdet)
    time.sleep(3)
    client1.publish('comm/msg4', signal)
    time.sleep(3)
    
