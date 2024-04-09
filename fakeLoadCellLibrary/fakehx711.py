import random

class hx711:
    def __init__(self) -> None:
        pass

    
    def begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN) -> None:
        """
        Function that creates the load cell object and gives it the correct pins
        Doesn't need to do anything as the load cell is simulated

                Parameters:
                        LOADCELL_DOUT_PIN arduino digital output pin used for the loadcell
                        LOADCELL_SCK_PIN arduino pin used for the clock

                Returns:
                        None
        """
        pass


    def set_scale() -> None:
        """
        Function that sets the scale for the load cell
        Doesn't need to do anything as the load cell is simulated

                Parameters:
                        None

                Returns:
                        None
        """
        pass

    def tare() -> None:
        """
        Function that tare the load cell

                Parameters:
                        None

                Returns:
                        None
        """
        pass
    
    
    def get_units() -> int:
        """
        Get's the weight from the load cell and returns it
        for this simulation a range from 0 to 1500 grams or 0 to 1.5l is used

            Parameters:
                    None

            Returns:
                    Returns the weight measured by the load cell
        """
        return random.randint(0, 1500)