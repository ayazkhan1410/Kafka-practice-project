import os

from dotenv import load_dotenv
from confluent_kafka import Consumer

load_dotenv()

# Consumer Configration
config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "twitter-profile-consumer",
    "auto.offset.reset": "earliest",
}

# Create Consumer
consumer = Consumer(config)

# Subscribe to topic
consumer.subscribe([os.getenv("TWITTER_PROFILE_BASE_TOPIC")])

print("Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0) # Polling for 1 second

        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        print(f"Received message: {msg.value().decode('utf-8')}")
        print(f"From Partition: {msg.partition()}")

except KeyboardInterrupt:
    print("Consumer stopped by user")
finally:
    consumer.close()
