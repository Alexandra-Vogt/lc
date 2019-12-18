#!/usr/bin/env python3

import lunar_functions as lf


def test_ladd():
    """Tests lunar addition."""
    assert lf.ladd(1, 22) == 22
    assert lf.ladd(278, 6556) == 6578
    assert lf.ladd(9999, 0000) == 9999
    print("ladd passed")


def test_lsum():
    """Tests lunar summation."""
    assert lf.lsum(1, 33, 456, 2313) == 2456
    print("lsum passed")


def test_lmul():
    """Tests lunar multiplication."""
    assert lf.lmul(17, 24) == 124
    assert lf.lmul(25, 235) == 2235
    print("lmul passed")


def test_lpow():
    """Tests lunar powers."""
    assert lf.lpow(5, 2) == lf.lmul(5, 5)
    assert lf.lpow(15, 3) == lf.lmul(lf.lmul(15, 15), 15)
    print("lpow passed")


test_ladd()
test_lsum()
test_lmul()
test_lpow()
