import os
import paho.mqtt.client as mqtt
import random
import json
import time

# MQTT settings
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")  # Docker service name
MQTT_PORT = 1883

# Topics
TOPICS = {
    "tracking": "luggage/tracking"
}

# Dictionary to store luggage data
luggage_data = {}

# Generate 1000 luggages with sequential IDs
def generate_luggage():
    luggages = []
    for luggage_id in range(1000):
        location = {'latitude': round(random.uniform(-90, 90), 6), 'longitude': round(random.uniform(-180, 180), 6)}
        size = {
            'length': round(random.uniform(30, 60), 2),
            'width': round(random.uniform(20, 40), 2),
            'height': round(random.uniform(30, 100), 2)
        }
        status = random.choice(["checked-in", "in-transit", "delivered"])
        weight = round(random.uniform(5, 30), 2)
        timestamp = int(time.time())
        
        luggage = {
            "id": luggage_id,
            "location": location,
            "size": size,
            "status": status,
            "weight": weight,
            "timestamp": timestamp
        }
        luggages.append(luggage)
        luggage_data[luggage_id] = luggage
    
    return luggages

# Update random location for a given luggage_id
def update_random_location(luggage_id):
    if luggage_id in luggage_data:
        last_location = luggage_data[luggage_id]['location']
        latitude = last_location['latitude'] + round(random.uniform(-0.5, 0.5), 6)
        longitude = last_location['longitude'] + round(random.uniform(-0.5, 0.5), 6)
        luggage_data[luggage_id]['location'] = {'latitude': latitude, 'longitude': longitude}
    else:
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        luggage_data[luggage_id] = {'location': {'latitude': latitude, 'longitude': longitude}}
    
    return luggage_data[luggage_id]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connect failed with code {rc}")

client = mqtt.Client()
client.on_connect = on_connect

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

client.loop_start()

# Generate initial luggage data
generate_luggage()

try:
    while True:
        if luggage_data:
            luggage_id = random.choice(list(luggage_data.keys()))
            luggage_updated = update_random_location(luggage_id)
            client.publish(TOPICS["tracking"], json.dumps(luggage_updated))
            print(f"Published to {TOPICS['tracking']}: {luggage_updated}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Script interrupted by user")
finally:
    client.loop_stop()
    client.disconnect()
