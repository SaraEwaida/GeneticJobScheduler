import tkinter as tk
from tkinter import scrolledtext
from genetic_algorithm import GeneticAlgorithm  # Assuming GeneticAlgorithm class manages the algorithm
from models import Job  # Ensure Job class is correctly imported from models.py
from visualizer import Visualizer  # Assuming you have visualizer.py setup

def generate_schedule(individual):
    schedule = {}
    for job in individual.genes:  # Correctly access genes of the Individual
        for operation in job.operations:
            machine_id, start_time, duration = operation
            end_time = start_time + duration
            if machine_id not in schedule:
                schedule[machine_id] = []
            schedule[machine_id].append((start_time, end_time, job.job_id))
    return schedule

def format_schedule_for_display(schedule):
    output_text = "#Best Schedule:\n"
    for machine, tasks in sorted(schedule.items()):
        output_text += f"Machine {machine}:\n"
        for start, end, job_id in tasks:
            output_text += f"-Job {job_id} on Machine {machine}: Start at {start}, Finish at {end}\n"
    return output_text

def run_algorithm():
    # Sample jobs setup
    jobs = [
        Job(1, [(1, 0, 10), (2, 10, 5), (4, 15, 12)]),
        Job(2, [(2, 0, 7), (3, 7, 15), (1, 22, 8)]),
        Job(3, [(1, 0, 9), (4, 9, 13), (2, 22, 6)])
    ]
    ga = GeneticAlgorithm(jobs, population_size=50, num_generations=100, mutation_rate=0.01)
    best_solution, detailed_chromosomes = ga.run()  # Unpack the results correctly

    # Generate schedule from the best solution found
    jobs_schedule = generate_schedule(best_solution)
    formatted_schedule = format_schedule_for_display(jobs_schedule)
    # Assuming you have a Gantt chart visualization
    Visualizer.plot_gantt_chart(jobs_schedule)

    # Display basic information about the best solution in the GUI
    output_text = f"Best Solution Fitness: {best_solution.fitness}\n\n#Best Schedule:\n"
    for machine, tasks in sorted(jobs_schedule.items()):
        output_text += f"Machine {machine}:\n"
        for start, end, job_id in sorted(tasks, key=lambda x: x[0]):
            output_text += f"-Job {job_id} on Machine {machine}: Start at {start}, Finish at {end}\n"

    output.delete('1.0', tk.END)
    output.insert(tk.END, output_text)

def setup_gui():
    root = tk.Tk()
    root.title("Genetic Algorithm for Job Scheduling")
    root.geometry("600x400")

    global output
    output = scrolledtext.ScrolledText(root, height=15)
    output.pack(pady=20)

    start_button = tk.Button(root, text="Start Genetic Algorithm", command=run_algorithm)
    start_button.pack(pady=10)

    return root

def main():
    app = setup_gui()
    app.mainloop()

if __name__ == "__main__":
    main()
