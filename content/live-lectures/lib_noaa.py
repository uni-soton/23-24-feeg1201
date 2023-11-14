#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:07:32 2023

@author: feeg1201
"""

"""
Lecture 04, 30 October 2023

Data engineering tasks
======================

- read NOAA data [1] on temperature anomaly from file
- make numbers available in lists
- display data in table
- retrieve temperature deviation for a given year

[1] https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/9/1850-2023/data.csv

"""


def plot_f(n_cols, xs, fs):
    """Plot f(x) in n_cols columns with one row
    per entry in the lists. We assume the values
    are equivally spaced in x-direction.
    """
    # check that both lists have the same length
    assert len(xs) == len(fs)
    for i in range(len(xs)):
        x = xs[i]
        fx = fs[i]
        # f(x) = -1  -> pos 0
        # f(x) = +1  -> pos n_cols
        max_fs = max(fs)
        min_fs = min(fs)
        pos = n_cols * (fx - min_fs) / (max_fs - min_fs)
        # create string s to print later
        s = int(pos) * " " + "+"
        print(f"{x}: " + s)


def read_data(filename):
    """Read data from comma seperated value file with format
    as the file from NOAA [1].

    Returns two lists: one for years and one for temps.
    """
    fh = open(filename, "rt")
    lines = fh.readlines()
    fh.close()

    result_years = []
    result_temps = []

    for line in lines[6:]:
        tmp = line.split(",")
        year = int(tmp[0])
        temp = float(tmp[1].rstrip())
        result_years.append(year)
        result_temps.append(temp)
    return result_years, result_temps


def display_lists(list1, list2):
    """Given two lists of equil length, print a
    table with the elements of the lists.
    """
    assert len(list1) == len(list2)
    for i in range(len(list1)):
        item1 = list1[i]
        item2 = list2[i]
        print(f"{item1} | {item2}")


def temperature_anomaly(year):
    """Given a year, return the temperature anomaly as specified
    in  the data file [1].
    """
    years, temps = read_data("data.csv")
    index = year - 1850
    assert year == years[index]

    return temps[index]


def temperature_anomaly_test():
    assert temperature_anomaly(1850) == -0.18
    assert temperature_anomaly(1851) == 0.02
    assert temperature_anomaly(2023) == 1.44


# always run tests: can we read the data file okay?
temperature_anomaly_test()
