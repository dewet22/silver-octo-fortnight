import pytest


@pytest.mark.usefixtures('db')
class TestUser:

    def test_basic_operations(self):
        pass
