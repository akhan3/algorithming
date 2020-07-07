import pytest
from two_sum_sorted import two_sum_sorted

# TODO: refactor ugly global variable
test_sorted = True


def two_sum_wrapper(nums, target):
    if test_sorted:
        nums.sort()
    return two_sum_sorted(nums, target)


def test_empty_match():
    assert two_sum_wrapper([], 0)


def test_empty_not_match():
    assert not two_sum_wrapper([], 5)


def test_1_length_match():
    assert two_sum_wrapper([4], 4)


def test_1_length_not_match():
    assert not two_sum_wrapper([4], 5)


def test_1_length_match_zero():
    assert two_sum_wrapper([4], 0)


def test_2_length_match():
    assert two_sum_wrapper([6, 4], 6)


def test_2_length_not_match():
    assert not two_sum_wrapper([6, 4], 5)


def test_5_length_match():
    assert two_sum_wrapper([8, 1, 6, 4, -3], 5)


def test_5_length_match_multiple():
    assert two_sum_wrapper([3, 1, 2, 4, -3], 5)


def test_5_length_not_match():
    assert not two_sum_wrapper([8, 1, 6, 4, -3], -40)


def test_5_length_match_zero():
    assert two_sum_wrapper([8, 1, 6, 4, -3], 0)


@pytest.mark.skip(reason="test case not written yet")
def test_some_repeated_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_repeated_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_unique_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_zeros_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_some_repeated_not_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_repeated_not_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_unique_not_match():
    pass


@pytest.mark.skip(reason="test case not written yet")
def test_all_zeros_not_match():
    pass
