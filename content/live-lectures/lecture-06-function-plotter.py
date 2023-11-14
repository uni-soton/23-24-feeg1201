"""Example for Lecture 06: function plotter."""
import math
import matplotlib.pyplot as plt
import numpy as np


def func_plotter(f, xmin, xmax, n_values):
    """Plot function f(x).

    Given a callable f, minimum (xmin) and maximum (xmax) values, and the
    number n_values of points to plot, plot a graph of f(x) where x starts
    at xmin and ranges up to and including xmax.
    """
    delta_x = (xmax - xmin)/(n_values-1)
    xs = [i*delta_x + xmin for i in range(n_values)]
    ys = [f(x) for x in xs]
    fig, ax = plt.subplots()
    ax.plot(xs, ys, '-o')
    ax.set_xlabel('x')
    ax.set_ylabel(f.__name__)
    return fig, ax

# %%


def func_plotter_np(f, xmin, xmax, n_values):
    """Plot function f(x).

    Given a callable f, minimum (xmin) and maximum (xmax) values, and the
    number n_values of points to plot, plot a graph of f(x) where x starts
    at xmin and ranges up to and including xmax.
    """
    xs = np.linspace(xmin, xmax, n_values)
    ys = f(xs)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, '-o')
    ax.set_xlabel('x')
    ax.set_ylabel(f.__name__)
    return fig, ax


def my_function(x):
    """Demo function."""
    return np.sin(x*5) * np.exp(-x/2)


# %%

func_plotter_np(np.sin, 0, 2*3.14, 10)

# %%

func_plotter(math.sin, 0, 2*3.14, 10)


# %%

func_plotter_np(my_function, 0, 10, 1000)
