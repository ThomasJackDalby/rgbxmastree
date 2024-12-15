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

client = mqtt.Client()

CURRENT_PATTERN = None
COMPONENTS = []

class SwitchComponent:

    def __init__(self, name, value=False):
        self.name = name
        self.value = value
        self.on_value_set = None
        self.full_name = f"dalby.rgbxmastree.{name}"
        self.config_topic = f"homeassistant/switch/{DEVICE_TYPE}/{name}/config"
        self.command_topic = f"dalby/{DEVICE_TYPE}/{name}/set"
        self.state_topic = f"dalby/{DEVICE_TYPE}/{name}/state"
        self.availability_topic = f"dalby/{DEVICE_TYPE}/{name}/available"
        self.payload_on = "on"
        self.payload_off = "off"
    
    def publish_config(self, client):
        config_payload ={
            "device": get_device_info(),
            "availability_topic": self.availability_topic,
            "unique_id": f"dalby/rgbxmastree/{self.name}",
            "state_topic": self.state_topic,
            "name": self.full_name,
            "device_class": "switch",
            "icon": "mdi:camera",
            "payload_on": self.payload_on,
            "payload_off": self.payload_off,
            "command_topic": self.command_topic
        }
        client.publish(
            topic=self.config_topic, 
            payload=json.dumps(config_payload), 
            qos=QOS, 
            retain=RETAIN
        )
    def publish_available(self, client):
        client.publish(self.availability_topic, "online")

    def publish_state(self, client):
        client.publish(self.state_topic, self.payload_on if self.value else self.payload_off)

def get_device_info():
    return {
            "identifiers": [
                "dalby_rgbxmastree"
            ],
            "name": "Raspberry Pi Rgb Xmas Tree"
        }

def register_component(name):
    component = SwitchComponent(name)
    COMPONENTS.append(component)
    return component

def on_connected(client, user_data, flags, result_code):
    for component in COMPONENTS:
        client.subscribe(component.command_topic)
        component.publish_config(client)
        component.publish_available(client)
        component.publish_state(client)

def on_message(client, user_data, message):
    global CURRENT_PATTERN
    for component in COMPONENTS:
        if message.topic == component.command_topic:
            component.value = not component.value
            component.publish_state(client)

            # if we're turning on one pattern, we need to turn off the others
            if component.value:
                CURRENT_PATTERN = component.name
                for other_component in COMPONENTS:
                    if component == other_component: continue
                    other_component.value = False
                    other_component.publish_state(client)

def connect():
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connected
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    return client