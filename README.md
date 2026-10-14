# Venue Crowd Flow Modelling – Event Ingress Case Study

## Project Overview

A Python-based crowd flow modelling project investigating how entrance capacity and attendee arrival patterns influence queue formation, waiting times and operational performance at live events.

The project combines a foundational entrance simulation with a fictional case study involving a venue hosting up to 3,000 attendees.

The objective is to demonstrate how mathematical modelling and scenario analysis can support event planning and operational decision-making.

## Project Structure

**Part 1 – Entrance Queue Simulation**

Developed an entrance queue model to explore the relationship between visitor arrivals, processing capacity and queue formation.

The simulation was used to compare different numbers of entrance lanes and investigate performance under variable conditions.

**Part 2 – Event Ingress Case Study**

Applied queue modelling to a fictional live-event scenario involving 3,000 attendees.

Investigated how arrival surges, security lane numbers and changes to arrival distribution could affect entrance congestion.

## Case Study Assumptions

| Parameter | Assumption |
|---|---|
| Maximum attendance | 3,000 |
| Gates open | 17:00 |
| Main act starts | 20:30 |
| Public entrance | 1 |
| Baseline security lanes | 4 |
| Ticket scanning points | 3 |

The scenario uses a simplified capacity-based queue model rather than a detailed pedestrian movement simulation.

## Scenarios Analysed

Four operational scenarios were compared:

1. **Baseline:** Four security lanes with the original arrival distribution.
2. **Increased capacity:** Five security lanes with the original arrivals.
3. **Improved arrivals:** Four lanes with attendees distributed more evenly across arrival periods.
4. **Combined improvements:** Five lanes alongside the revised arrival distribution.

## Results

| Scenario | Peak Queue | Maximum Estimated Wait | Final Queue |
|---|---:|---:|---:|
| Baseline – 4 lanes | 810 | 50.6 min | 300 |
| 5 lanes | 450 | 22.5 min | 0 |
| Improved arrivals | 410 | 25.6 min | 150 |
| Combined improvements | 310 | 19.4 min | 0 |

## Key Findings

- The baseline scenario experienced significant queue formation during peak arrival periods.
- Increasing the number of security lanes improved entrance processing capacity.
- Redistributing attendee arrivals reduced peak congestion without increasing lane numbers.
- Combining both changes produced the lowest peak queue and estimated waiting time among the four scenarios.

The combined scenario reduced the peak queue from 810 to 310 people, a reduction of approximately 61.7%.

## Skills Demonstrated

- Python programming
- Queue modelling and simulation
- Mathematical and quantitative analysis
- Scenario comparison
- Operational capacity analysis
- Data visualisation
- Decision-support modelling

## Limitations

This project uses fictional event data and simplified processing-capacity assumptions. It is designed to demonstrate a modelling and analytical methodology rather than provide a validated operational assessment.

Factors such as physical crowd density, individual walking behaviour, security processing variability and interactions between entrance stages are not fully represented.

## Running the Project

The repository contains two Python scripts:

- `part_1_entrance_simulation.py` – Foundational entrance simulation.
- `part_2_event_ingress_case_study.py` – Application to the fictional event and scenario comparison.

Open and run the scripts using a Python environment such as Spyder, with any required dependencies installed.

## Conclusion

The case study demonstrates how relatively simple simulation models can help identify potential queue bottlenecks and compare the effectiveness of operational changes before an event takes place.
