
import random
import matplotlib.pyplot as plt

# Set the basic venue values
lane_capacity = 8
lane_options = [2, 3, 4, 5, 6]

# Store results for each lane option
lane_results = []


# Calculate how many people can enter per minute
def calculate_capacity(number_lanes, lane_capacity):
    return number_lanes * lane_capacity


# Calculate the queue after each minute
def calculate_queue(current_queue, total_capacity, arrivals):
    return max(0, current_queue + arrivals - total_capacity)


# Compare each entrance setup
for number_of_lanes in lane_options:

    # Reset results for this lane option
    peak_queues = []
    total_times = []

    total_capacity = calculate_capacity(
        number_of_lanes,
        lane_capacity
    )

    # Run 100 simulations
    for simulation in range(100):

        arrivals_per_minute = []
        current_queue = 0
        max_queue = 0

        # Create a random arrival pattern
        for minute in range(1, 16):

            if minute <= 5:
                arrivals = random.randint(15, 25)

            elif minute <= 10:
                arrivals = random.randint(45, 55)

            else:
                arrivals = random.randint(10, 20)

            arrivals_per_minute.append(arrivals)

        # Simulate the queue minute by minute
        for minute, arrivals in enumerate(
            arrivals_per_minute,
            start=1
        ):

            current_queue = calculate_queue(
                current_queue,
                total_capacity,
                arrivals
            )

            if current_queue > max_queue:
                max_queue = current_queue

        # Continue until the queue is empty
        while current_queue > 0:
            minute += 1

            current_queue = calculate_queue(
                current_queue,
                total_capacity,
                0
            )

        # Save this simulation's results
        peak_queues.append(max_queue)
        total_times.append(minute)

    # Calculate averages for this lane option
    average_peak_queue = (
        sum(peak_queues) / len(peak_queues)
    )

    average_total_time = (
        sum(total_times) / len(total_times)
    )

    # Save the comparison result
    lane_results.append([
        number_of_lanes,
        round(average_peak_queue, 2),
        round(average_total_time, 2)
    ])

# Show the final comparison
print("\nLane comparison")

for result in lane_results:
    print(
        result[0], "lanes -",
        "Average peak queue:", result[1],
        "- Average entry time:", result[2], "minutes"
    )

#Extract results for plotting
lanes = [result[0] for result in lane_results]
average_queues = [result[1] for result in lane_results]

# Plot lanes against average peak queue
plt.plot(lanes, average_queues, marker="o")

plt.xlabel("Number of entrance lanes")
plt.ylabel("Average peak queue")
plt.title("Effect of Entrance Lanes on Peak Queue")

plt.show()

# Extract average entry times
average_times = [result[2] for result in lane_results]

# Plot lanes against average entry time
plt.plot(lanes, average_times, marker="o")

plt.xlabel("Number of entrance lanes")
plt.ylabel("Average entry time (minutes)")
plt.title("Effect of Entrance Lanes on Entry Time")

plt.show() 

# Calculate improvement between lane setups
for i in range(1, len(lane_results)):

    previous_queue = lane_results[i - 1][1]
    current_queue = lane_results[i][1]

    improvement = (
        (previous_queue - current_queue)
        / previous_queue
        * 100
    )

    print(
        lane_results[i - 1][0], "to",
        lane_results[i][0], "lanes -",
        round(improvement, 1), "% reduction in peak queue"
    )