def mysum1(n):
    """Given a natural number n > 0,
    compute the sum of numbers from i=0
    up to and including i=n.
    """
    s = 0  # store my sum here

    # loop over i, starting from i=1, ending with i=n:
    for i in range(1, n + 1):
        s = s + i
    return s


print("mysum1(3) is", mysum1(3))
