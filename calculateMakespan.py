def calculateMakespan(times, machines, config, n):
    # Initialize availability times for all machines
    machine_availability = {machine: 0 for sublist in machines for machine in sublist}
    schedules = {machine: [] for sublist in machines for machine in sublist}
    job_end_times = [0] * n
    makespan = 0

    for job_index in range(n):
        start_time = 0
        for operation_index, machine_id in enumerate(machines[job_index]):
            start_time = max(start_time, machine_availability[machine_id])  # Ensure machine is available
            duration = times[job_index][operation_index]
            end_time = start_time + duration
            machine_availability[machine_id] = end_time
            job_end_times[job_index] = end_time
            schedules[machine_id].append((start_time, end_time, f"Job {job_index + 1}"))

            # Update makespan
            makespan = max(makespan, end_time)

    return makespan, schedules

