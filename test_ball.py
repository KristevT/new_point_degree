import pytest
from ball_degree import degree

test_degree = (
    (3.0, 0.0, 5.0, 2.0, 191.08),
    (7.0, 0.0, 4.0, 0.0, 0.0),
    (7.0, -5.0, 4.0, 1.0, 65.19),
    (1.0, 0.0, 0.0, 0.0, 0.0),
    (3.0, 3.0, 2.0, 9.0, 98.6),
)

@pytest.mark.parametrize("radius, acceleration, time, velocity, expected", test_degree)
def test_degrees(radius: float, acceleration: float, time: float, velocity: float, expected: float) -> None:
    assert degree(radius, acceleration, time, velocity) == expected
