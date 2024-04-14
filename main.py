from util import Pins
from waterLevelSensor import LoadCell
from waterPumpElement import Pump
from waterHeatingElement import Heating
import logger as log
import unittest
from tests import *
from simulator import simulator

import ctypes
import pathlib

#library for the hx711 but since this load cell is simulated it won't be used yet
#include "HX711.h"
# fake hx711 library for simulation purpose
from fakeLoadCellLibrary.fakehx711 import hx711


if __name__ == '__main__':
    libname = pathlib.Path().absolute()
    print("libname: ", libname)
    pathstring = str(libname)
    # Load the shared library into c types.
    c_lib = ctypes.CDLL(pathstring+"/libtempSensor.so")

    c_lib.request_temperature_from_sensor.restype = ctypes.c_float
    
    # Giving the function the D3 pin to make the onewire bus on
    temperature = c_lib.request_temperature_from_sensor(Pins.D3.value)
    print(f"temperature: {temperature:.1f}")
    
    print("|-----------------------------------------|")
    
    # Executing the load cell functions and showing the log
    scale = hx711
    loadcell_element = LoadCell()
    loadcell_element.set_scale(scale)
    loadcell_element.tare(scale)
    waterlevel = loadcell_element.get_units(scale)
    print("Waterlevel: ",waterlevel)
    log.show_log()
    print("|-----------------------------------------|")
    
    relay_pin_1 = Pins.D1
    relay_pin_2 = Pins.D2
    min_waterlevel_pump = 100
    min_waterlevel_heat = 1000
    max_waterlevel = 1500
    max_temperature = 100

    pump_element = Pump()
    heating_element = Heating()
    
    pump_element.set_pinmode(relay_pin_1)
    heating_element.set_pinmode(relay_pin_2)
    
    print("Temperature: ", temperature)
    print("Waterlevel: ", waterlevel)
    
    if heating_element.control_heat(temperature, max_temperature, waterlevel, min_waterlevel_heat, relay_pin_1):
        print("heating is turned on")
    else:
        print("heating is turned off")
        
    if pump_element.control_pump(waterlevel, min_waterlevel_pump, max_waterlevel, relay_pin_2):
        print("heating is turned on")
    else:
        print("heating is turned off")
        
    print("|-----------------------------------------|")
    log.show_log()