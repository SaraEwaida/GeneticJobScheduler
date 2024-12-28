class Job:
    def __init__(self, job_id, operations):
        """
        Initializes a Job instance with a unique identifier and a list of operations.
        """
        self.job_id = job_id
        if all(isinstance(op, tuple) and len(op) == 3 for op in operations):
            self.operations = operations
        else:
            raise ValueError("Operations should be a list of tuples (machine_id, start_time, duration)")

    def get_operation_times(self):
        return [op[2] for op in self.operations]

    def get_operation_machines(self):
        return [op[0] for op in self.operations]

    def __repr__(self):
        return f"Job(Job ID: {self.job_id}, Operations: {self.operations})"

class Machine:
    def __init__(self, machine_id):
        """
        Initializes a Machine instance with an identifier.
        """
        self.machine_id = machine_id
        self.schedule = []

    def allocate_job(self, start_time, job, duration):
        if any(s[0] <= start_time < s[1] for s in self.schedule):
            raise ValueError("Attempted to schedule an overlapping job on the machine.")
        end_time = start_time + duration
        self.schedule.append((start_time, end_time, job.job_id))
        return end_time

    def __repr__(self):
        return f"Machine(ID: {self.machine_id}, Scheduled Tasks: {len(self.schedule)})"
