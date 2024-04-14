from fakeArduinoLibrary.fakeArduino import *
from logger import log_arguments
from timing import time_function

class Pump:
    """ Contains functions to control a relay which then controls the pump element
    """
    
    def __init__(self) -> None:
        return
    
    @time_function
    @log_arguments
    def set_pinmode(self, relay_pin) -> None:
        """
        Sets the pump element relay pin to output mode

                Parameters:
                        None

                Returns:
                        None
        """
        pinMode(relay_pin, OUTPUT)
        return
    
    @time_function
    @log_arguments
    def control_pump(self, water_level, min_waterlevel, max_waterlevel, relay_pin) -> int:
        """
        decides whether the pump needs to be turned on or off and will do so if found to be neccesary

                Parameters:
                        water_level: how much water is already inside the kettle
                        min_waterlevel: if water_level is below this it means that the kettle is not on the loadcell and the pump cannot turn on
                        max_waterlevel: how much water is allowed to be pumped into the kettle
                        relay_pin: the pin the pump relay is connected to

                Returns:
                        0: if the pump is turned off
                        1: if the pump is turned on
        """
        if water_level < min_waterlevel:
            return self.pump_off(relay_pin)
        elif water_level >= min_waterlevel and water_level < max_waterlevel:
            return self.pump_on(relay_pin)
        elif water_level >= max_waterlevel:
            return self.pump_off(relay_pin)

    @time_function
    @log_arguments
    def pump_on(self, relay_pin) -> int:
        """
        Turns off the pump element relay which turns off the pump element. It returns a 1 as feedback of the pump elements state

                Parameters:
                        None

                Returns:
                        1 to indicate it has turned the pump element off
        """
        digitalWrite(relay_pin, HIGH)
        return 1
    
    @time_function
    @log_arguments
    def pump_off(self, relay_pin):
        """
        Turns off the pump element relay which turns off the pump element. It returns a 0 as feedback of the pump elements state

                Parameters:
                        None

                Returns:
                        0 to indicate it has turned the pump element off
        """
        digitalWrite(relay_pin, LOW)
        return 0
