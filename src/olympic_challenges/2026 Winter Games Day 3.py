"""
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.
* Each round consists of 5 targets.
* Each missed target results in a 150 meter penalty loop
"""


def calculate_penalty_distance(rounds):
    total_missed = sum(5 - hits for hits in rounds)
    return total_missed * 150

** end of main.py **

