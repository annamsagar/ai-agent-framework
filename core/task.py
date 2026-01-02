class Task:
    """
    Represents a single executable step in a workflow.
    A task wraps an agent and defines what task(s) run next.
    """

    def __init__(self, name, agent, next_tasks=None):
        self.name = name
        self.agent = agent
        self.next_tasks = next_tasks or []
