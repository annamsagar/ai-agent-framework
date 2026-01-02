import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def emit_event(event):
    """
    Send an event to Kafka topic: agent-events
    """
    producer.send("agent-events", event)
    producer.flush()
