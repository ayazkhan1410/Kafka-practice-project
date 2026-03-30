# Kafka Practice Project

A simple Kafka-based producer and consumer implementation using Python and `confluent-kafka`.

## Features
- **Producer**: Sends Twitter profile data to a Kafka topic.
- **Consumer**: Listens for messages on the specified Kafka topic and prints them.
- **Interactive UI**: `app.py` allows manual entry of profile details to be sent.

## Prerequisites
- Python 3.x
- Apache Kafka running on `localhost:9092` (or as configured in `.env`)

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**:
   Create a `.env` file in the root directory (referencing `.env.example` if available) with the following variables:
   ```env
   KAFKA_BOOTSTRAP_SERVERS=localhost:9092
   KAFKA_TOPIC=your_topic_name
   TWITTER_PROFILE_BASE_TOPIC=twitter_profile_events
   ```

## Usage

1. **Start the Consumer**:
   Run the consumer in a separate terminal to listen for events:
   ```bash
   python consumer.py
   ```

2. **Run the Application (Producer)**:
   Run `app.py` to send profile events:
   ```bash
   python app.py
   ```
   Follow the prompts to enter a target URL and name.
