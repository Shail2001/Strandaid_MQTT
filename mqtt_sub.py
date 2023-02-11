import time
import paho.mqtt.client as mqtt

print ('\nMessage from Queen Drone!')
print ('\nStart Flight!')

def on_message(client1, userdata, message1):
   print ('\nMessage from Queen Drone!')
   
   print ('\nBattery Remaining: ', message1.payload) 

broker_address = '192.168.0.101'
client1 = mqtt.Client("SUB1")
client1.on_message = on_message
client1.connect(broker_address) 
client1.loop_start()
client1.subscribe('comm/msg1')

def on_message(client2, userdata, message2):
   print ('\nMessage from Queen Drone!')
   print ('\nObstacle Detected... Drone Movement: ', message2.payload) 

#broker_address = '127.0.1.1'
client2 = mqtt.Client("SUB2")
client2.on_message = on_message
client2.connect(broker_address) 
client2.loop_start()
client2.subscribe('comm/msg2')

def on_message(client3, userdata, message3):
   print ('\nMessage from Queen Drone!')
   print ('\n', message3.payload) 

#broker_address = '127.0.1.1'
client3 = mqtt.Client("SUB3")
client3.on_message = on_message
client3.connect(broker_address) 
client3.loop_start()
client3.subscribe('comm/msg3')

def on_message(client4, userdata, message4):
   print ('\nMessage from Queen Drone!')
   print ('\n', message4.payload) 

#broker_address = '127.0.1.1'
client4 = mqtt.Client("SUB4")
client4.on_message = on_message
client4.connect(broker_address) 
client4.loop_start()
client4.subscribe('comm/msg4')

#qbat = 100
try:
   while True:
      #client.publish('test/qbattery', qbat)
      #qbat -= 0.25
      time.sleep(5)

except KeyboardInterrupt:
   client.loop_stop()
   pass 

