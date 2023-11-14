"""
Write a python function `plot_sin()`
which plots a sin wave f(x) = sin(x) like
this (x going down, f(x) to the right):


                                         +
                                                 +
                                                           +
                                                                   +
                                                                         +
                                                                             +
                                                                              +
                                                                              +
                                                                            +
                                                                      +
                                                               +
                                                      +
                                             +
                                  +
                         +
                +
         +
   +
+
+
 +
      +
            +
                    +
                              +
"""
import math

import matplotlib.pyplot as plt


def plot_sin(n_rows, n_cols):
    """Plot sin wave f(x)=sin(x) in n_rows rows and n_cols columns.

    Example: plot_sin(25, 50)
    """
    for i in range(n_rows):
        x = i / n_rows * 2 * math.pi
        fx = math.sin(x)  # compute f(x)
        # f(x) = -1  -> pos 0
        # f(x) = +1  -> pos 80
        pos = n_cols * (fx + 1) / 2
        # create string s to print later
        s = int(pos) * " " + "+"
        print(s)


def compute_sin(n):
    """Returns lists xs and fs=sin(xs) with n data points.
    """
    results_xs = []
    results_sin = []
    for i in range(n):
        x = i / n * 2 * math.pi
        sin_x = 2*math.sin(x)  # compute f(x)
        results_xs.append(x)
        results_sin.append(sin_x)
    return results_xs, results_sin


def plot_f(n_cols, xs, fs):
    """Plot f(x) in n_cols columns.
    Expects two lists xs and fs with x-values and function values,
    respectively. Lists need to have same length.
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
        print(f"{x:7f}: " + s)



# compute data for sine wave
my_xs, my_fs = compute_sin(20)

fig, ax = plt.subplots()
ax.plot(my_xs, my_fs, 'o-g')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("My first plot")
# ax.set_x


# plt.close('all')




# plot the data
# plot_f(n_cols=40, xs=my_xs, fs=my_fs)
