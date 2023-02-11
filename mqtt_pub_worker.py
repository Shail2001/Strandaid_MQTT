import time
import paho.mqtt.client as mqtt
from random import seed
from random import randint

broker_address = "127.0.1.1"

#Topic-1 Client
client1 = mqtt.Client("PUB1W")
client1.connect(broker_address)

wbat = 100
direction = ["Moved to Left Side", "Moved to Right Side", "Elevation", "Decline"]
signal = "Sending Signal... Distance from Drone: 6 meters"

while True:
    client1.publish('comm/msg1w', wbat)
    wbat -= 0.25
    time.sleep(3)
    indexValue = randint(0,3)
    movement = direction[indexValue]
    client1.publish('comm/msg2w', movement)
    time.sleep(3)
    client1.publish('comm/msg3w', signal)
    time.sleep(3)
    