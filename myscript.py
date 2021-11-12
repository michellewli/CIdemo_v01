import sys

def sayhi(s):
    print('Hello, ', s)
    print('Python version is ,' sys.version)
    return None

def test_sayhi():
    assert True


def test_other():
    assert False
