#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collection of samll utilities we may need in multiple programs.

Hans Fangohr, for FEEG1201, Nov 2023
"""


def compute_average(xs):
    """Expect list of numbers `xs`. Then compute and return
    the average of those numbers. Need at least one element in the list.
    """
    return sum(xs) / len(xs)


def test_compute_average():
    assert compute_average([0]) == 0
    assert compute_average([-1, 0, 1]) == 0
    assert compute_average([1, 1, 1]) == 1
    assert compute_average([10, 20, 30]) == 20


# always (when imported) execute tests for now
test_compute_average()
