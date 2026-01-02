import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "agent-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("📡 Listening for agent events...")

for message in consumer:
    print("EVENT:", message.value)
