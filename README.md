# GeneticJobScheduler
Optimizing Job Shop Scheduling in a Manufacturing Plant Using a Genetic Algorithm

**Project Overview**
The GeneticJobScheduler is a system designed to optimize job shop scheduling in a manufacturing plant using a genetic algorithm. The system is capable of efficiently scheduling multiple jobs across various machines with the goal of minimizing the overall production time and enhancing machine utilization.

**Features**
Data Structures: The project defines structured data representations for jobs and machines.
Genetic Algorithm: Implements a genetic algorithm to optimize scheduling, including components such as initialization, fitness evaluation, selection, crossover, mutation, and replacement.
Visualization: Incorporates visual tools to display the scheduling results, including a Gantt chart that offers a clear visual representation of the jobs scheduled over time.

**Technologies Used**
Python
Matplotlib and Plotly for visualization
Tkinter for the user interface

**Getting Started**
To run the GeneticJobScheduler, follow these steps:
Clone the Repository
bash
Copy code
git clone https://github.com/SaraEwaida/GeneticJobScheduler.git
Install Required Libraries
Copy code
pip install matplotlib plotly
Run the Application Navigate to the cloned directory and run:
css
Copy code
python main.py

**How It Works**
Data Input: The user can input the number of jobs, the number of machines, and specific job requirements.
Algorithm Execution: The genetic algorithm processes the input to determine the optimal scheduling.
Output Display: The results are displayed both textually and visually via a Gantt chart.

**Example Output**
The output of the GeneticJobScheduler is presented in two formats to provide a clear and comprehensive view of the optimized job scheduling:
Textual Output: Displays detailed scheduling information including start and end times for each job on respective machines.
Gantt Chart: Offers a visual representation of the scheduling across machines, illustrating the timing and duration of each job operation. 
This visualization helps in quickly understanding the distribution and overlap of job schedules, facilitating easier analysis of the scheduling efficiency.

**Future Enhancements**
Integrate more complex job dependencies.
Improve the genetic algorithm's efficiency with advanced genetic operations.

