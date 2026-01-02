from core.state import State

# 🔗 Kafka integration (Member 2)
from infra.kafka_producer import emit_event
from infra.events import build_event


class Orchestrator:
    """
    Executes a Flow by running tasks in order,
    managing state, audit logs, and emitting Kafka events.
    """

    def run(self, flow, input_data):
        state = State(flow.name)
        state.data["input"] = input_data

        current_task = flow.start_task

        while current_task:
            task = flow.tasks[current_task]
            agent_input = state.data.copy()

            # 🔔 EVENT: Task Started
            emit_event(
                build_event(state.flow_id, current_task, "STARTED")
            )

            try:
                output = task.agent.run(agent_input)

                # Record execution
                state.record(
                    task=current_task,
                    input_data=agent_input,
                    output_data=output
                )

                # 🔔 EVENT: Task Completed
                emit_event(
                    build_event(state.flow_id, current_task, "COMPLETED")
                )

                # Move to next task
                current_task = task.next_tasks[0] if task.next_tasks else None

            except Exception as e:
                # 🔔 EVENT: Task Failed
                emit_event(
                    build_event(state.flow_id, current_task, "FAILED")
                )
                raise e

        # Save audit logs
        state.save()
        return state.data
