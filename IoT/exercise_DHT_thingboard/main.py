import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient
import json

#THIS IS WOKWI PROJECT

# MQTT Server Parameters
MQTT_CLIENT_ID = "datle"
MQTT_BROKER    = "app.coreiot.io"
MQTT_USER      = "" #ACCESS TOKEN HERE
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "v1/devices/me/telemetry"
RPC_TOPIC      = "v1/devices/me/rpc/request/+"

power_pin = Pin(25, Pin.OUT)

def on_message(topic, msg):
    # print("Received message:", msg)
    try:
        # Parse the incoming JSON message
        data = json.loads(msg)
        
        # Check if the RPC method is 'togglePower'
        if 'method' in data and data['method'] == "setState":
            if data['params']:
                power_pin.on()
            else:
                power_pin.off()

    except Exception as e:
        print("Error processing message:", e)

sensor = dht.DHT22(Pin(32))

print("WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

print("MQTT....", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(on_message)

client.connect()

client.subscribe(RPC_TOPIC)
print("Connected!")

while True:
  sensor.measure() 
  message = ujson.dumps({
    "temperature": sensor.temperature(),
    "humidity": sensor.humidity(),
  })
  
  print("Send {}".format(message))
  client.publish(MQTT_TOPIC, message)
  client.check_msg()
  time.sleep(0.3)
