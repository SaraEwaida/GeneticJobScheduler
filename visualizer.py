import plotly.figure_factory as ff

class Visualizer:
    @staticmethod
    def plot_gantt_chart(schedule):
        df = []
        colors = {}  # To store colors for each job
        color_palette = ['#333F44', '#93e4c1', '#FFD700', '#FF6347', '#4682B4']  # Example color palette

        # Prepare data for the Gantt chart
        for machine, tasks in schedule.items():
            for start, end, job_id in tasks:
                resource_key = f"Job {job_id}"  # Ensure this matches how you define jobs in your schedule
                df.append(dict(Task=f"Machine {machine}", Start=start, Finish=end, Resource=resource_key))
                if resource_key not in colors:
                    colors[resource_key] = color_palette[len(colors) % len(color_palette)]

        # Create Gantt chart
        fig = ff.create_gantt(df, colors=[colors[d['Resource']] for d in df], index_col='Resource', show_colorbar=True,
                              group_tasks=True)
        fig.update_layout(title='Job Shop Scheduling Gantt Chart', xaxis_title='Time', yaxis_title='Machines')
        fig.show()
