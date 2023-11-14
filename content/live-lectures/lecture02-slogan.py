
""" Our task:

Hypothetical scenario:

We are software engineers and acting on behalf of an advertising
agency. Our task is to compute the cost to print a slogan onto a
large billboard. The companies owners tell us that the cost is
computed as the daily rate (that's a number, for example 10 GBP)
times the square of the number of vowels in the slogan.

For example: in the slogan "Just do it", we have 3 vowels ('u',
'o' and 'i'), so the cost would be 10 GBP * (3*3) = 90 GBP.
"""


def count_vowels(s):
    """Return the number of vowels in string s."""
    s_lower = s.lower()
    a = s_lower.count("a")
    e = s_lower.count("e")
    i = s_lower.count("i")
    o = s_lower.count("o")
    u = s_lower.count("u")
    return a + e + i + o + u


def square(x):
    """Given x, return x*x."""
    return x * x


def compute_cost(slogan, daily_rate):
    """Compute and return the cost of string 'slogan' for 'daily_rate'...
    """
    return daily_rate * square(count_vowels(slogan))


print(compute_cost("Python is awesome", 20))
print(compute_cost("Just do it", 10))
