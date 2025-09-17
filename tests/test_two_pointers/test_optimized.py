import pytest
from src.two_pointers.optimized import find_target_some_pair


@pytest.mark.parametrize(
    "arr, target_sum, expected",
    [
        # ✅ Positive numbers only
        ([1, 2, 3, 4, 5, 6], 3, [(1, 2)]),  # single pair
        ([1, 2, 3, 4, 5, 6], 7, [(1, 6), (2, 5), (3, 4)]),  # multiple pairs
        ([1, 2, 3, 4, 5, 6], 11, [(5, 6)]),  # upper boundary
        ([1, 2, 3, 4, 5, 6], 20, []),  # no result
        # ✅ Negative numbers only
        (
            [-6, -5, -4, -3, -2, -1],
            -7,
            [(-6, -1), (-5, -2), (-4, -3)],
        ),  # multiple neg pairs
        ([-6, -5, -4], -20, []),  # impossible target
        # ✅ Mixed positive + negative
        ([-3, -2, -1, 1, 2, 3], 0, [(-3, 3), (-2, 2), (-1, 1)]),  # crossing zero
        ([-3, -2, -1, 1, 2, 3], 5, [(2, 3)]),  # only positives add up
        ([-3, -2, -1, 1, 2, 3], -5, [(-3, -2)]),  # only negatives add up
        # ✅ Corner cases
        ([], 5, []),  # empty list
        ([5], 5, []),  # single element
        ([1, 2], 3, [(1, 2)]),  # Double With match element
        ([1, 2], 1, []),  # Double element without match
        ([0, 0, 0], 0, [(0, 0), (0, 0), (0, 0)]),  # multiple zeros
    ],
    ids=[
        "pos-single-pair",
        "pos-multiple-pairs",
        "pos-upper-boundary",
        "pos-no-result",
        "neg-multiple-pairs",
        "neg-no-result",
        "mixed-cross-zero",
        "mixed-pos-only",
        "mixed-neg-only",
        "corner-empty-list",
        "corner-single-element",
        "corner-double-element",
        "corner-double-element-without-match",
        "corner-multiple-zeros",
    ],
)
def test_find_target_some_pair(arr, target_sum, expected):
    result = find_target_some_pair(arr, target_sum)
    assert sorted(result) == sorted(expected)
