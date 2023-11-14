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


plot_sin(25, 30)
