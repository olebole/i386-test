import sys


def test_pysize():
    assert sys.maxsize < 2**32
