import math

def circle(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be positive.

    Returns:
        float: The area of the circle.

    Raises:
        TypeError: If the radius is not positive.
    """
    radius = float(radius)
    if radius <= 0:
        raise TypeError("Radius must be positive")
    return math.pi * radius ** 2

def square(side: float) -> float:
    """
    Calculate the area of a square given its side length.

    Args:
        side (float): The length of one side of the square. Must be positive.

    Returns:
        float: The area of the square.

    Raises:
        TypeError: If the side length is not positive.
    """
    side = float(side)
    if side <= 0:
        raise TypeError("Values must be positive")
    return side * side

def rectangle(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle. Must be positive.
        width (float): The width of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle.

    Raises:
        TypeError: If either the length or width is not positive.
    """
    length = float(length)
    width = float(width)
    if length <= 0 or width <= 0:
        raise TypeError("Values must be positive")
    return length * width

def triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given its base and height.

    Args:
        base (float): The base of the triangle. Must be positive.
        height (float): The height of the triangle. Must be positive.

    Returns:
        float: The area of the triangle.

    Raises:
        TypeError: If either the base or height is not positive.
    """
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise TypeError("Values must be positive")
    return 0.5 * base * height
