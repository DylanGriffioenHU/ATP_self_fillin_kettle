from fakeArduinoLibrary.fakeArduino import *
from logger import log_arguments


class Pump:
    def __init__(self, relay_pin, minimum_waterlevel, maximum_waterlevel) -> None:
        self.relay_pin = relay_pin
        self.minimum_waterlevel = minimum_waterlevel
        self.maximum_waterlevel = maximum_waterlevel
        return
    
    @log_arguments
    def setup(self) -> None:
        """
        Sets the pump element relay pin to output mode

                Parameters:
                        None

                Returns:
                        None
        """
        pinMode(self.relay_pin, OUTPUT)
        return
    
    @log_arguments
    def control_pump(self, water_level, pump_state) -> int:
        """
        decides whether the pump needs to be turned on or off and will do so if found to be neccesary

                Parameters:
                        water_level: this function needs the water level measured by waterLevelSensor.py
                        pump_state: this function needs to know what state the pump is in

                Returns:
                        0: if the pump is turned off
                        1: if the pump is turned on
                        pump_state: if the function doesn't end up changing the pump stat for whatever reason it will return the pump stat variable
        """
        if water_level < self.minimum_waterlevel:
            if pump_state:
                return self.pumpOff()
        elif water_level >= self.minimum_waterlevel and water_level < self.maximum_waterlevel:
            if not pump_state:
                return self.pumpOn()
        elif water_level >= self.maximum_waterlevel:
            if pump_state:
                return self.pumpOff()
        return pump_state

    @log_arguments
    def pumpOn(self) -> int:
        """
        Turns on the pump element relay which turns on the pump element

                Parameters:
                        None

                Returns:
                        1 to provide feedback on the pumps state
        """
        digitalWrite(self.relay_pin, HIGH)
        return
    
    @log_arguments
    def pumpOff(self):
        """
        Turns off the pump element relay which turns off the pump element

                Parameters:
                        None

                Returns:
                        0 to provide feedback on the pumps state
        """
        digitalWrite(self.relay_pin, LOW)
        return 0
