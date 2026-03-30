import os
import json
import traceback

from confluent_kafka import Producer
from dotenv import load_dotenv
from producer import delivery_report

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Producer configuration
config = {
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
}

producer = Producer(config)

def send_youtube_profile_event(profile_data):
    try:
        topic = os.getenv("YOUTUBE_PROFILE_BASE_TOPIC")
        payload = json.dumps(profile_data).encode("utf-8")
        producer.produce(topic, payload, callback=delivery_report)
        producer.flush()
    except Exception as e:
        traceback.print_exc()
        print(f"Error sending profile event: {e}")
        raise e


if __name__ == "__main__":
    target_url = input("Enter the Youtube target URL: ")
    target_name = input("Enter the Youtube target name: ")

    test_data = {
        "target_url": target_url,
        "target_name": target_name,
    }

    # Send profile event
    print("================================================")
    print("Sending Youtube profile event...")
    send_youtube_profile_event(test_data)
    print("================================================")
    print("Youtube profile event sent successfully")
    print("================================================")
