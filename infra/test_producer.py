from kafka_producer import emit_event
from events import build_event

emit_event(build_event("flow1", "task1", "STARTED"))
emit_event(build_event("flow1", "task1", "COMPLETED"))

print("Events sent successfully")
