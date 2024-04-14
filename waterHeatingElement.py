from fakeArduinoLibrary.fakeArduino import *
from logger import log_arguments
from timing import time_function

# class containing functions to control the heating element for the kettle
class Heating:
    """ Contains functions to control a relay which then controls the heating element
    """
    
    def __init__(self) -> None:
        return
    
    @time_function
    @log_arguments
    def set_pinmode(self, relay_pin):
        """
        puts the given pin into output mode

                Parameters:
                        relay_pin: the pin the pump relay is connected to

                Returns:
                        None
        """
        pinMode(relay_pin, OUTPUT)
        return

    @time_function
    @log_arguments
    def control_heat(self, temperature, max_temperature, water_level, min_waterlevel, relay_pin):
        """
        decides whether the heating needs to be turned on or off and will do so if found to be neccesary

                Parameters:
                        temperature: the temperature of the water you want the heating element to heat
                        max_temperature: the maximum temperature you want the water to get heated to
                        water_level: how much water is already inside the kettle
                        min_waterlevel: the mimimum amount of water that needs to be inside of the kettle before the heating is allowed to turn on
                        relay_pin: the pin the heating relay is connected to

                Returns:
                        0: if the heating is turned off
                        1: if the heating is turned on
        """
        if water_level < min_waterlevel:
            return self.heat_off(relay_pin)
        elif temperature < max_temperature:
            return self.heat_on(relay_pin)
        elif temperature >= max_temperature:
            return self.heat_off(relay_pin)
    
    @time_function
    @log_arguments
    def heat_on(self, relay_pin) -> int:
        """
        Turns on the heating element relay which turns on the heating element. It returns a 1 as feedback of the heating elements state

                Parameters:
                        None

                Returns:
                        1 to indicate it has turned the heating element on
        """
        digitalWrite(relay_pin, HIGH)
        return 1 # not really needed but it provides usefull feedback to the rest of the program

    @time_function
    @log_arguments
    def heat_off(self, relay_pin):
        """
        Turns off the heating element relay which turns off the heating element. It returns a 0 as feedback of the heating elements state

                Parameters:
                        None

                Returns:
                        0 to indicate it has turned the heating element off
        """
        digitalWrite(relay_pin, LOW)
        return 0 # not really needed but it provides usefull feedback to the rest of the program
