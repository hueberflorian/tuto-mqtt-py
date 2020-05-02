# MQTT Tutorial in Python Copyright © 2020 HUEBER Florian

# Libraries
import paho.mqtt.client as mqtt
import json

# TO COMPLETE-----------------------
id = 'blabla'
pwd = 'blabla'
topic = "blabla"
# ----------------------------------

# Creating JSON
payload = {"x": 160, "y": 180, "direction": 275}

# Serializing the data to json format (same as stringify function in js)
payload = json.dumps(payload)

# Show the JSON
print("JSON ready to be published: ")
print(payload)


# Subscribing and Publishing to a topic of the broker
def on_connect(client, userdata, flags, rc):
    # RC means Result Code
    # Output: Connected with result code 0 means no error
    print(" ")
    print("Connected with result code " + str(rc))

    # Subscribing
    client.subscribe(topic)

    # Publishing the payload to the topic
    client.publish(topic, payload)


# Receiving the payload
def on_message(client, userdata, msg):
    # Decoding function
    a = str(msg.payload.decode())
    # Show the output
    print(" ")
    print("Received payload: ")
    print(a)

    print(" ")
    print("Converting from Json to Object")
    # Decode json data (same as parse in js)
    recu = json.loads(a)
    # Show the type of recu
    print(type(recu))
    # recu is a dictionnary so we then show all the values
    print("Position X: ", recu["x"])
    print("Position Y: ", recu["y"])
    print("Direction: ", recu["direction"])


# Declaration of the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# id and pwd to connect to the broker
client.username_pw_set(id, pwd)
# URL to connect to the broker
client.connect("foundation.lyon.ece.licot.fr", 2019, 60)

# Repeat the program
client.loop_forever()
