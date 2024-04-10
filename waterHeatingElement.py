from fakeArduinoLibrary.fakeArduino import *
from logger import log_arguments
from util import Pins

# class containing functions to controll the heating element for the kettle
class Heating:
    relay = Pins.D4

    def __init__(self, maximum_temerature, minimum_waterlevel) -> None:
        self.maximum_temerature = maximum_temerature
        self.minimum_waterlevel = minimum_waterlevel
        return

    # Sets the relay pin to output mode
    @log_arguments
    def setup(self) -> None:
        """
        Sets the heating element relay pin to output mode

                Parameters:
                        None

                Returns:
                        None
        """
        pinMode(self.relay, OUTPUT)
        pass

    def control_heat(self, heat, water_level, heat_state):
        if water_level < self.minimum_waterlevel:
            if heat_state:
                return self.heatOff()
        elif heat < self.maximum_temerature:
            if not heat_state:
                return self.heatOn()
        elif heat >= self.maximum_temerature:
            if heat_state:
                return self.heatOff()

    @log_arguments
    def heatOn(self) -> int:
        """
        Turns on the heating element relay which turns on the heating element

                Parameters:
                        None

                Returns:
                        1 which is not needed but provides feedback to the main program
        """
        digitalWrite(self.relay, HIGH)
        return 1

    @log_arguments
    def heatOff(self):
        """
        Turns off the heating element relay which turns off the heating element

                Parameters:
                        None

                Returns:
                        0 which is not needed but provides feedback to the main program
        """
        digitalWrite(self.relay, LOW)
        return 0
