from core.state import State


class Orchestrator:
    """
    Executes a Flow by running tasks in order,
    managing state and audit logs.
    """

    def run(self, flow, input_data):
        # Initialize state
        state = State(flow.name)
        state.data["input"] = input_data

        # Start execution from the defined start task
        current_task = flow.start_task

        while current_task:
            task = flow.tasks[current_task]

            # Provide full state snapshot to the agent
            agent_input = state.data.copy()

            # Execute agent
            output = task.agent.run(agent_input)

            # Record execution
            state.record(
                task=current_task,
                input_data=agent_input,
                output_data=output
            )

            # Move to next task (simple linear execution)
            current_task = task.next_tasks[0] if task.next_tasks else None

        # Persist audit logs
        state.save()

        return state.data
