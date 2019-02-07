import pytest

from person import Person


@pytest.fixture()
def person_without_address():
    return Person('Alexandr', 1799)  # year can be string


@pytest.fixture()
def person():
    return Person('Alexandr', 1799, 'Moscow')  # year can be string


def test_default_initial_address(person_without_address):
    assert person_without_address.address == ''
