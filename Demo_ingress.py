
# Arrival numbers and time periods
arrivals = [300, 600, 900, 750, 300, 150]
better_arrivals = [450, 600, 650, 600, 450, 250]
combined_arrivals = [250, 400, 550, 650, 550, 400, 200]

times = ["17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]
combined_times = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]

# Times used for comparison chart
all_times = ["17:00","17:30", "18:00", "18:30","19:00","19:30","20:00"]

# Calculate the queue after each time period
def calculate_queue(current_queue, arrivals, capacity):
    return max(0, current_queue + arrivals - capacity)


# Run one entrance scenario
def run_scenario(name, arrivals, times, capacity):
    queue = 0
    queue_results = []

    print(f"\n{name}")

    # Work through each time period
    for people, time in zip(arrivals, times):
        queue = calculate_queue(queue, people, capacity)
        queue_results.append(queue)
        print(f"{time} - Queue: {queue}")

    # Find the largest queue
    peak_queue = max(queue_results)

    # Estimate the maximum waiting time
    people_per_minute = capacity / 30
    max_wait = peak_queue / people_per_minute

    # Return the main results
    return peak_queue, max_wait, queue, queue_results


# --------------------
# RUN SCENARIOS
# --------------------

# Baseline - 4 lanes
peak_4, wait_4, final_4, results_4 = run_scenario(
    "4 Security Lanes",
    arrivals,
    times,
    480
)

# Extra capacity - 5 lanes
peak_5, wait_5, final_5, results_5 = run_scenario(
    "5 Security Lanes",
    arrivals,
    times,
    600
)

# Better arrival pattern
peak_better, wait_better, final_better, results_better = run_scenario(
    "4 Lanes - Better Arrival Pattern",
    better_arrivals,
    times,
    480
)

# Better arrivals and earlier opening
peak_combined, wait_combined, final_combined, results_combined = run_scenario(
    "4 Lanes - Better Arrivals + Earlier Opening",
    combined_arrivals,
    combined_times,
    480
)


# --------------------
# COMPARE RESULTS
# --------------------

print("\nScenario Comparison")

print(
    f"4 lanes - Peak queue: {peak_4}, "
    f"Max wait: {wait_4:.1f} mins, "
    f"Final queue: {final_4}"
)

print(
    f"5 lanes - Peak queue: {peak_5}, "
    f"Max wait: {wait_5:.1f} mins, "
    f"Final queue: {final_5}"
)

print(
    f"Better arrivals - Peak queue: {peak_better}, "
    f"Max wait: {wait_better:.1f} mins, "
    f"Final queue: {final_better}"
)

print(
    f"Combined changes - Peak queue: {peak_combined}, "
    f"Max wait: {wait_combined:.1f} mins, "
    f"Final queue: {final_combined}"
)


# Compare better arrivals against the baseline
queue_reduction = ((peak_4 - peak_better) / peak_4) * 100
wait_reduction = ((wait_4 - wait_better) / wait_4) * 100

print(f"\nPeak queue reduction: {queue_reduction:.1f}%")
print(f"Max wait reduction: {wait_reduction:.1f}%")

import matplotlib.pyplot as plt

# Peak queue comparison chart
scenario_names = [
    "4 lanes",
    "5 lanes",
    "Better arrivals",
    "Combined changes"
]

peak_queues = [
    peak_4,
    peak_5,
    peak_better,
    peak_combined
]

plt.bar(scenario_names, peak_queues)
plt.title("Peak Queue by Scenario")
plt.ylabel("People in Queue")
plt.show()

results_4_chart = [0] + results_4
results_5_chart = [0] + results_5
results_better_chart = [0] + results_better

# Queue over time chart
plt.plot(all_times, results_4_chart, marker="o", label="4 lanes")
plt.plot(all_times, results_5_chart, marker="o", label="5 lanes")
plt.plot(all_times, results_better_chart, marker="o", label="Better arrivals")
plt.plot(all_times, results_combined, marker="o", label="Combined changes")

plt.title("Queue Size Over Time")
plt.xlabel("Time")
plt.ylabel("People in Queue")
plt.legend()
plt.grid(True)
plt.show()