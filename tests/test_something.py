import pytest


@pytest.mark.usefixtures('db')
class TestSomething:

    def test_one_thing(self):
        pass

    def test_another_thing(self):
        pass

    def test_a_third_thing(self):
        pass
