import paho.mqtt.client as mqtt
import json
import serial
import threading
from datetime import datetime
import asyncio

ser = serial.Serial('COM4', 9600)  # Replace COM3 with the correct port
on_time = off_time = None

def on_message(client, userdata, msg):
     global on_time, off_time
     data = json.loads(msg.payload.decode())
     on_time = data['on']
     off_time = data['off']
     print(f"Updated ON: {on_time}, OFF: {off_time}")

def scheduler():
     global on_time, off_time
     while True:
          now = datetime.now().strftime("%H:%M")
          if now == on_time:
               print("Turning ON light")
               ser.write(b'1')
          elif now == off_time:
               print("Turning OFF light")
               ser.write(b'0')
          asyncio.sleep(30)

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("light/schedule")

threading.Thread(target=scheduler, daemon=True).start()
client.loop_forever()
