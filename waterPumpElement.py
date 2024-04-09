from fakeArduinoLibrary.fakeArduino import *
from util import Pins

class Pump:
    relay = Pins.D5

    def __init__(self) -> None:
        pass

    def setup(self) -> None:
        """
        Sets the pump element relay pin to output mode

                Parameters:
                        None

                Returns:
                        None
        """
        pinMode(self.relay, OUTPUT)
        pass
    
    def pumpOn(self) -> int:
        """
        Turns on the pump element relay which turns on the pump element

                Parameters:
                        None

                Returns:
                        1 which is not needed but provides feedback to the main program
        """
        digitalWrite(self.relay, HIGH)
        return 1
    
    def pumpOff(self):
        """
        Turns off the pump element relay which turns off the pump element

                Parameters:
                        None

                Returns:
                        0 which is not needed but provides feedback to the main program
        """
        digitalWrite(self.relay, LOW)
        return 0
