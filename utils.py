import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from matplotlib.cm import get_cmap  # Correct import for getting a colormap


def plot_gantt_chart(jobs, title='Gantt Chart'):
    """
    Plots a Gantt chart based on the given jobs schedule.
    Jobs can be a dictionary with two possible formats:
    1. {machine: [(start, duration, job_id), ...]}
    2. {machine: [(start, end, job_id), ...]}
    """
    fig, ax = plt.subplots()
    num_jobs = sum(len(tasks) for tasks in jobs.values())
    color_map = get_cmap('viridis')  # Correctly get the 'viridis' colormap
    colors = color_map(np.linspace(0, 1, num_jobs))  # Generate colors for each job

    color_idx = 0  # Initialize color index
    for machine, tasks in jobs.items():
        for start, second_value, job_id in tasks:
            if isinstance(start, (float, int)):  # Assume start time is provided as a float or int
                start = datetime.now() + timedelta(seconds=start)  # Convert to datetime
            if isinstance(second_value, (float, int)):
                end = start + timedelta(seconds=second_value)
            else:
                end = second_value

            duration = (end - start).total_seconds() / 3600.0  # Duration in hours
            ax.barh(machine, duration, left=start, height=0.4, color=colors[color_idx], edgecolor='black')
            mid_point = start + timedelta(seconds=(end - start).total_seconds() / 2)
            ax.text(mid_point, machine, f'Job {job_id}', ha='center', va='center', color='white')
            color_idx += 1

    ax.set_xlabel('Time')
    ax.set_yticks([i for i, _ in enumerate(jobs)])
    ax.set_yticklabels([machine for machine in jobs])
    ax.set_title(title)
    plt.tight_layout()
    plt.show()

