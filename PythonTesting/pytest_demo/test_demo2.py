import pytest


def test_first():
    print("Hello")


def test_second():
    print("Second test Log")


@pytest.mark.Smoke
def test_third():
    print("Smoke Test Log")


def test_main(handle):
    print("inside main")
