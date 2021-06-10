import pytest


@pytest.mark.usefixtures("handle")
class TestAbc:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")