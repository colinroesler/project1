from area import *

class Calculator:
    def __init__(self) -> None:
        """
        Initialize the calculator with a default mode set to 'area'.
        """
        self.mode: str = 'area'

    def set_mode(self, mode: str) -> None:
        """
        Set the calculator's mode.

        Args:
            mode (str): The mode to set. Currently, only 'area' is supported.

        Raises:
            ValueError: If the provided mode is not supported.
        """
        if mode not in ['area']:
            raise ValueError("Invalid mode. Supported modes: 'area'")
        self.mode = mode

    def compute_area(self, shape: str, *args: float) -> float:
        """
        Compute the area based on the specified shape.

        Args:
            shape (str): The type of shape ('circle', 'square', 'rectangle', 'triangle').
            *args (float): The dimensions of the shape.
                - Circle: radius (1 argument)
                - Square: side length (1 argument)
                - Rectangle: width and height (2 arguments)
                - Triangle: base and height (2 arguments)

        Returns:
            float: The calculated area of the shape.

        Raises:
            ValueError: If the calculator is not in 'area' mode.
            ValueError: If the shape is not supported or if the wrong number of arguments are provided.
        """
        if self.mode != 'area':
            raise ValueError("Calculator is not in 'area' mode.")

        # Match the shape and call function from the area module
        if shape == 'circle':
            if len(args) != 1:
                raise ValueError("Circle requires 1 argument: radius.")
            return circle(args[0])
        elif shape == 'square':
            if len(args) != 1:
                raise ValueError("Square requires 1 argument: side length.")
            return square(args[0])
        elif shape == 'rectangle':
            if len(args) != 2:
                raise ValueError("Rectangle requires 2 arguments: width and height.")
            return rectangle(args[0], args[1])
        elif shape == 'triangle':
            if len(args) != 2:
                raise ValueError("Triangle requires 2 arguments: base and height.")
            return triangle(args[0], args[1])
        else:
            raise ValueError("Invalid shape. Supported shapes: circle, square, rectangle, triangle.")
