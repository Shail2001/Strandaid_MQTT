import time
import paho.mqtt.client as mqtt

print ('\nMessage from Worker Drone!')
print ('\nMessage Received Ready to Go!')

def on_message(client1, userdata, message1):
   print ('\nMessage from Worker Drone!')
   print ('\nBattery Remaining: ', message1.payload) 

broker_address = '127.0.1.1'
client1 = mqtt.Client("SUB1W")
client1.on_message = on_message
client1.connect(broker_address) 
client1.loop_start()
client1.subscribe('comm/msg1w')

def on_message(client2, userdata, message2):
   print ('\nMessage from Worker Drone!')
   print ('\nObstacle Detected... Drone Movement: ', message2.payload) 

client2 = mqtt.Client("SUB2W")
client2.on_message = on_message
client2.connect(broker_address) 
client2.loop_start()
client2.subscribe('comm/msg2w')

def on_message(client3, userdata, message3):
   print ('\nMessage from Worker Drone!')
   print ('\n', message3.payload) 

client3 = mqtt.Client("SUB3W")
client3.on_message = on_message
client3.connect(broker_address) 
client3.loop_start()
client3.subscribe('comm/msg3w')

try:
   while True:
      time.sleep(5)

except KeyboardInterrupt:
   client.loop_stop()
   pass 

