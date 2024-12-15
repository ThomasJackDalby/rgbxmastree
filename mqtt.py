import os
import json
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
load_dotenv()

MQTT_HOST = os.getenv('MQTT_HOST')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
MQTT_PORT = 1883

QOS = 2
RETAIN = False

DEVICE_TYPE = "rgbxmastree"

ENABLED_CONFIG_TOPIC = f"homeassistant/switch/{DEVICE_TYPE}/Enabled/config"
ENABLED_COMMAND_TOPIC = f"dalby/{DEVICE_TYPE}/Enabled/set"
ENABLED_STATE_TOPIC = f"dalby/{DEVICE_TYPE}/Enabled/state"
ENABLED_AVAILIBILITY_TOPIC = f"dalby/{DEVICE_TYPE}/Enabled/available"

enabled = False

def send_configuration_topic(client):
    config_payload ={
        "device": {
            "identifiers": [
                "dalby_rgbxmastree"
            ],
            "name": "Raspberry Pi Rgb Xmas Tree"
        },
        "availability_topic": ENABLED_AVAILIBILITY_TOPIC,
        "unique_id": "dalby/rgbxmastree/Enabled",
        "state_topic": ENABLED_STATE_TOPIC,
        "name": "dalby.rgbxmastree.Enabled",
        "device_class": "switch",
        "icon": "mdi:camera",
        "payload_on": "on",
        "payload_off": "off",
        "command_topic": ENABLED_COMMAND_TOPIC
    }
    client.publish(
        topic=ENABLED_CONFIG_TOPIC, 
        payload=json.dumps(config_payload), 
        qos=QOS, 
        retain=RETAIN
    )

def on_connected(client, user_data, flags, result_code):
    client.subscribe(ENABLED_COMMAND_TOPIC)
    send_configuration_topic(client)
    client.publish(ENABLED_AVAILIBILITY_TOPIC, "online")

def on_message(client, user_data, message):
    if message.topic == ENABLED_COMMAND_TOPIC:
        client.publish(ENABLED_STATE_TOPIC, "on" if enabled else "off")

def connect():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connected
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    return client