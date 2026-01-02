import time

def build_event(flow_id, task, status):
    return {
        "flow_id": flow_id,
        "task": task,
        "status": status,   # STARTED | COMPLETED | FAILED
        "timestamp": time.time()
    }
