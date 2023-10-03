import paho.mqtt.client as mqtt
import time

# MQTT broker settings
broker_address = "localhost"
port = 1883

# Client ID (change this for each client)
client_id = "Client1"

# Topic for the chat
chat_topic = "chat"

# Dictionary to store cached messages with timestamps
message_cache = {}

# Callback when a message is received
def on_message(client, userdata, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    message_cache[timestamp] = message.payload.decode()
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' at {timestamp}")

# Initialize the MQTT client
client = mqtt.Client(client_id)

# Set the message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Subscribe to the chat topic
client.subscribe(chat_topic)

# Start the MQTT client loop
client.loop_start()

# Main loop
while True:
    message = input("Enter a message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    # Publish the message to the chat topic
    client.publish(chat_topic, message)

# Disconnect from the broker and stop the MQTT client loop
client.disconnect()
client.loop_stop()
