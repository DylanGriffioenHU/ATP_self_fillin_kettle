#library for the hx711 but since this load cell is simulated it won't be used yet
#include "HX711.h"

from util import Pins
from logger import log_arguments

# fake hx711 library for simulation purpose
from fakeLoadCellLibrary.fakehx711 import hx711

class LoadCell:
    # HX711 circuit wiring
    LOADCELL_DOUT_PIN = Pins.D2;
    LOADCELL_SCK_PIN = Pins.D3;
    scale = hx711

    def __init__(self) -> None:
        pass

    def setup(self):
        """
        Function that creates the load cell object and gives it the correct pins

                Parameters:
                        None

                Returns:
                        None
        """
        self.scale.begin(self.LOADCELL_DOUT_PIN, self.LOADCELL_SCK_PIN);
        pass
    
    
    def set_scale(self) -> None:
        """
        Function that sets the scale for the load cell

                Parameters:
                        None

                Returns:
                        None
        """
        self.scale.set_scale()
        pass


    def tare(self) -> None:
        """
        Function that tare the load cell

                Parameters:
                        None

                Returns:
                        None
        """
        self.scale.tare()
        pass    

    @log_arguments
    def get_units(self) -> int:
        """
        Get's the weight from the load cell and returns it

        Parameters:
                None

        Returns:
                Returns the weight measured by the load cell
        """
        return self.scale.get_units()
