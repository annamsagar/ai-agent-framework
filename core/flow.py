class Flow:
    """
    Defines an agentic workflow as a collection of tasks
    and a starting task.
    """

    def __init__(self, name):
        self.name = name
        self.tasks = {}
        self.start_task = None

    def add_task(self, task):
        """
        Add a task to the flow.
        """
        self.tasks[task.name] = task

    def set_start(self, task_name):
        """
        Define the starting task of the workflow.
        """
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' not found in flow")
        self.start_task = task_name
