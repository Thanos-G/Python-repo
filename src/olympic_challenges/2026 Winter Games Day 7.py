"""
Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, the second to lap 2, and so on.
"""


def largest_difference(skater1, skater2):

    max_diff = 0
    max_lap = 1
    for lap_index, (time1, time2) in enumerate(zip(skater1, skater2), start=1):
        diff = abs(time1 - time2)

        if diff > max_diff:
            max_diff = diff
            max_lap = lap_index

    return max_lap


** end of main.py **

