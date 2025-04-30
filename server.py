import asyncio
import websockets
import json
import subprocess

MQTT_TOPIC = "light/schedule"

async def handler(websocket, _):
     async for message in websocket:
          data = json.loads(message)
          payload = json.dumps(data)
          print(f"Received schedule: {payload}")

          # Send via mosquitto_pub
          subprocess.run(["mosquitto_pub", "-t", MQTT_TOPIC, "-m", payload])

start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
