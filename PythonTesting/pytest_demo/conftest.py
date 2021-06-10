import pytest


@pytest.fixture()
def handle():
    print("Open Browser")
    yield
    print("Close Browser")
