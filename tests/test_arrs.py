from utils import arrs
import pytest

@pytest.fixture
def array_fixture():
    return [1, 2, 3]


def test_get(array_fixture):
    assert arrs.get(array_fixture, 0, "test") == 1
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice(array_fixture, None) == [1, 2, 3]