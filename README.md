# GeneticJobScheduler
Optimizing Job Shop Scheduling in a Manufacturing Plant Using a Genetic Algorithm

## Project Overview
The GeneticJobScheduler is a system designed to optimize job shop scheduling in a manufacturing plant using a genetic algorithm. The system is capable of efficiently scheduling multiple jobs across various machines with the goal of minimizing the overall production time and enhancing machine utilization.

## Features
- **Data Structures**: The project defines structured data representations for jobs and machines.
- **Genetic Algorithm**: Implements a genetic algorithm to optimize scheduling, including components such as initialization, fitness evaluation, selection, crossover, mutation, and replacement.
- **Visualization**: Incorporates visual tools to display the scheduling results, including a Gantt chart that offers a clear visual representation of the jobs scheduled over time.

## Technologies Used
- Python
- Matplotlib and Plotly for visualization
- Tkinter for the user interface

## Getting Started
To run the GeneticJobScheduler, follow these steps:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/SaraEwaida/GeneticJobScheduler.git

2. Install Required Libraries
3. Copy code
4. pip install matplotlib plotly
5. Run the Application Navigate to the cloned directory and run:
- css
- Copy code
- python main.py

## How It Works

- **Data Input**: The user can input the number of jobs, the number of machines, and specific job requirements.
- **Algorithm Execution**: The genetic algorithm processes the input to determine the optimal scheduling. The results are displayed both textually and visually via a Gantt chart.

## Detailed Input and Output
- **Input Description**: The system takes as input a list of jobs and the number of available machines. Each job is defined as a sequence of operations, specifying the machine and the required processing time. For example:
Job_1: M1[10] -> M2[5] -> M4[12] Job_2: M2[7] -> M3[15] -> M1[8]
You can provide these inputs through the command line or a user interface.

- **Output Description**: The output is a detailed schedule for each machine, showing the start and end times for each process and to which job each process belongs. This scheduling is visualized using a Gantt chart, which helps in understanding the machine utilization and job overlaps.

## Testing and Demo
- **System Testing**: To test the system, specify the number of machines and a list of jobs through the provided interface. Sample commands and expected outputs are provided in the documentation.
- **Demo Preparation**: Be prepared to present a live demo of the project during evaluation. The demo will include a walkthrough of the code, the input process, and how the scheduling results are displayed.

## Submission Details
- This repository contains the source code necessary for the project along with detailed documentation on the implementation of the genetic algorithm, including chromosome representation, crossover, mutation, and the objective function used.
- A comprehensive report is available detailing the problem formulation and test cases, fulfilling the project's documentation requirement.

## Example Output

The output of the GeneticJobScheduler is presented in two formats to provide a clear and comprehensive view of the optimized job scheduling:
- **Textual Output**: Displays detailed scheduling information including start and end times for each job on respective machines.
- **Gantt Chart**: Offers a visual representation of the scheduling across machines, illustrating the timing and duration of each job operation. This visualization helps in quickly understanding the distribution and overlap of job schedules, facilitating easier analysis of the scheduling efficiency.

## Future Enhancements

- Integrate more complex job dependencies.
- Improve the genetic algorithm's efficiency with advanced genetic operations.
- Explore the addition of real-time adjustments to scheduling based on dynamic job priorities or machine availability.



