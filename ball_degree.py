def degree(radius: float, acceleration: float, time: float, velocity: float = 0):
    """Finds the displacement degree of the point of initial contact with the surface.

    Args:
        radius: float - radius of the rolling ball,
        acceleration: float - acceleration of the ball movement,
        time: float - time given for ball to roll,
        velocity: float - velocity of the ball movement,

    Returns:
        degree: float - displacement degree of the point."""

    s = velocity * time + (acceleration * (time ** 2)) / 2
    c = 2 * 3.14 * radius
    new_degree = round(((s % c) / c) * 360, 2)
    return new_degree
