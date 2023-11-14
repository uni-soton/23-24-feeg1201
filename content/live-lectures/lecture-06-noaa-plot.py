"""Lecture 06: demo plotting of data.

Use functions from lib_noaa library.
"""

import matplotlib.pyplot as plt
import lib_noaa as noaa
from lib_tools import compute_average


def average_by_decade(years, temps):
    """Compute average for each decade.

    Ignore years at end of period if
    they do not form a full decade. Return values are tuple of lists,
    containing the beginning of the decade and the average temperature
    deviation over the decade.
    """
    assert len(years) == len(temps)
    decades = len(years) // 10  # number of decades
    a_temps = []  # Averages temps
    a_years = []  # years for which average is computed
    for decade in range(decades):
        a_temp = compute_average(temps[decade * 10:(decade + 1) * 10])
        a_year = years[decade * 10 + 5]
        a_temps.append(a_temp)
        a_years.append(a_year)

    return a_years, a_temps


def plot_anomaly1():
    years, temps = noaa.read_data("data.csv")
    aves_year, aves = average_by_decade(years, temps)
    fig, ax = plt.subplots()
    ax.plot(years, temps, "o", alpha=0.3, label="temperature anomaly")
    ax.plot(aves_year, aves, "og-", label="10 year average")
    ax.legend()
    ax.set_xlabel("year")
    ax.set_ylabel("temperature anomaly [deg C]")


def plot_anomaly2():
    years, temps = noaa.read_data("data.csv")
    aves_year, aves = average_by_decade(years, temps)
    fig, ax = plt.subplots()
    ax.plot(years, temps, "og",  alpha=0.5)
    ax.plot(aves_year, aves, "-", linewidth=10, alpha=0.5,
            label="10 year average")
    ax.set_xlabel("year")
    ax.set_ylabel("temperature anomaly [deg C]")
    ax.legend()


def plot_anomaly3():
    years, temps = noaa.read_data("data.csv")
    aves_year, aves = average_by_decade(years, temps)
    fig, ax = plt.subplots()
    ax.plot(years, temps, "og", alpha=0.5)
    ax.bar(aves_year, aves, alpha=0.5, width=9.5, label="10 year average")
    ax.set_xlabel("year")
    ax.set_ylabel("temperature anomaly [deg C]")
    ax.legend()


plot_anomaly1()
plot_anomaly2()
plot_anomaly3()
