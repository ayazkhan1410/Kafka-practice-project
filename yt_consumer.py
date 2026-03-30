import os

from dotenv import load_dotenv
from confluent_kafka import Consumer

load_dotenv()

# Youtube Consumer Configration
config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "youtube-profile-consumer",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(config)

consumer.subscribe([os.getenv("YOUTUBE_PROFILE_BASE_TOPIC")])

print("Waiting for messages in Youtube consumer...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        print(f"Received message in youtube consumer: {msg.value().decode('utf-8')}")
        print(f"From Partition in youtube consumer: {msg.partition()}")

except KeyboardInterrupt:
    print("Consumer stopped by user")
finally:
    consumer.close()
