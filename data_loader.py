from models import Job
class DataLoader:
    @staticmethod
    def load_data(filepath):
        """
        Loads and parses job and machine data from a file.

        Args:
            filepath (str): The path to the data file.

        Returns:
            list: A list of Job objects initialized with data from the file.
        """
        jobs = []
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split()
                job_id = int(parts[0])
                operations = []
                for i in range(1, len(parts), 3):
                    machine_id = int(parts[i])
                    start_time = int(parts[i+1])
                    duration = int(parts[i+2])
                    operations.append((machine_id, start_time, duration))
                jobs.append(Job(job_id, operations))
        return jobs
