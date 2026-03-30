import os
import json

from dotenv import load_dotenv
from confluent_kafka import Consumer

load_dotenv()

# Consumer Configuration
# Using a different group.id allows this consumer to receive all messages 
config = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    "group.id": "twitter-profile-consumer-secondary",
    "auto.offset.reset": "earliest",
}

# Create Consumer
consumer = Consumer(config)

# Subscribe to topic
topic = os.getenv("TWITTER_PROFILE_BASE_TOPIC")
consumer.subscribe([topic])

print(f"Secondary Consumer started. Listening on topic: {topic}...")
print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0) # Polling for 1 second

        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        # Decode and process message
        data = json.loads(msg.value().decode('utf-8'))
        print("\n--- Secondary Consumer Received ---")
        print(f"Message: {data}")
        print(f"From Topic: {msg.topic()}")
        print(f"Partition: {msg.partition()}")
        print(f"Offset: {msg.offset()}")
        print("-----------------------------------\n")

except KeyboardInterrupt:
    print("Secondary Consumer stopped by user")
finally:
    consumer.close()
