from logger import log_arguments

class LoadCell:
    def __init__(self) -> None:
        return
    
    @log_arguments
    def setup(self, scale, LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN):
        """
        Function that creates the load cell object and gives it the correct pins

                Parameters:
                        None

                Returns:
                        None
        """
        scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
        return
    
    @log_arguments
    def set_scale(self, scale) -> None:
        """
        Function that sets the scale for the load cell

                Parameters:
                        None

                Returns:
                        None
        """
        scale.set_scale()
        return
    
    @log_arguments
    def tare(self, scale) -> None:
        """
        Function that tare the load cell

                Parameters:
                        None

                Returns:
                        None
        """
        scale.tare()
        return
    
    @log_arguments
    def get_units(self, scale) -> int:
        """
        Get's the weight from the load cell and returns it

        Parameters:
                None

        Returns:
                Returns the weight measured by the load cell
        """
        return scale.get_units()
