"""Ball movement module."""


def degree(radius: float, acceleration: float, time: float, velocity: float = 0):
    """Finds the displacement degree of the point.

    Args:
        radius: float - radius of the rolling ball,
        acceleration: float - acceleration of the ball movement,
        time: float - time given for ball to roll,
        velocity: float - velocity of the ball movement,

    Returns:
        degree: float - displacement degree of the point."""

    if radius == 0:
        return 0
    distance = velocity * time + (acceleration * (time ** 2)) / 2
    circle_length = 2 * 3.14 * radius
    new_degree = round(((distance % circle_length) / circle_length) * 360, 2)
    return new_degree
