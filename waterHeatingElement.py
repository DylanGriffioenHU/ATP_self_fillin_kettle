from fakeArduinoLibrary.fakeArduino import *
from util import Pins

# class containing functions to controll the heating element for the kettle
class Heating:
    relay = Pins.D4

    def __init__(self) -> None:
        pass

    # Sets the relay pin to output mode
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
