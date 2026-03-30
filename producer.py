import os
import json
import traceback

from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Producer configuration
config = {
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
}

producer = Producer(config)
print(f"Bootstrap Server from ENV: {os.getenv('KAFKA_BOOTSTRAP_SERVERS')}")


def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()}")
        print(f"Partition: {[msg.partition()]}")


def send_profile_event(profile_data):
    try:
        # Get topic from environment variable
        topic = os.getenv("TWITTER_PROFILE_BASE_TOPIC")

        # Convert dict to JSON
        payload = json.dumps(profile_data).encode("utf-8")

        # Send message to Kafka
        producer.produce(
            topic,
            payload,
            callback=delivery_report
        )

        # Flush producer
        producer.flush()
    except Exception as e:
        traceback.print_exc()
        print(f"Error sending profile event: {e}")
        raise e
