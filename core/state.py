import time
import json
import uuid
import os


class State:
    """
    Holds workflow state and execution audit logs.
    """

    def __init__(self, flow_name):
        self.flow_id = str(uuid.uuid4())
        self.flow_name = flow_name
        self.data = {}
        self.audit_log = []

    def record(self, task, input_data, output_data):
        """
        Record execution details of a task.
        """
        self.audit_log.append({
            "task": task,
            "input": input_data,
            "output": output_data,
            "timestamp": time.time()
        })
        self.data[task] = output_data

    def save(self):
        """
        Persist audit logs to disk.
        """
        os.makedirs("storage", exist_ok=True)
        with open(f"storage/{self.flow_id}.json", "w") as f:
            json.dump(self.audit_log, f, indent=2)
