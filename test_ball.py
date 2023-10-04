"""Test to degree function."""

import pytest

from ball_degree import degree

test_degree = (
    ((3.0, 0, 5.0, 2.0), 190.99),
    ((7.0, 0, 4.0, 0), 0),
    ((7.0, -5.0, 4.0, 1.0), 65.34),
    ((1.0, 0, 0, 0), 0),
    ((3.0, 3.0, 2.0, 9.0), 98.37),
)


@pytest.mark.parametrize('angle, expected', test_degree)
def test_degrees(angle: float, expected: float) -> None:
    """Test your degree function.

    Args:
        angle: float - tests data
        expected: float - expected result

    Asserts:
        float angle of shifting the ball.
    """
    assert degree(*angle) == expected
