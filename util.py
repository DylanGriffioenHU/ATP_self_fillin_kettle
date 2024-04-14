from enum import Enum

# This keeps the pins for the different components neatly in the same location in case one of them needs to be moved to a different pin
class Pins(Enum):
    """Contains digital pins that can be used throughout the project to connect the elements to

    Args:
        Enum (int): digital pin number
    """
    D1 = 22
    D2 = 23
    D3 = 24
    D4 = 25
    D5 = 26