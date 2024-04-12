from util import Pins
from waterLevelSensor import LoadCell
from waterPumpElement import Pump
from waterHeatingElement import Heating
import logger as log
import unittest
from tests import *
from simulator import simulator

#library for the hx711 but since this load cell is simulated it won't be used yet
#include "HX711.h"
# fake hx711 library for simulation purpose
from fakeLoadCellLibrary.fakehx711 import hx711


if __name__ == '__main__':
    # Set up the tests
    test_loader = unittest.TestLoader()
    test1 = test_loader.loadTestsFromTestCase(Test1_control_heating_element)
    test2 = test_loader.loadTestsFromTestCase(Test2_control_pump_element)
    test3 = test_loader.loadTestsFromTestCase(Test3_control_heating_element_with_waterlevel)
    test4 = test_loader.loadTestsFromTestCase(Test4_control_heat_and_waterlevel)

    # Run the tests and show the logs
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test1)
    log.show_log()
    result2 = test_runner.run(test2)
    log.show_log()
    result3 = test_runner.run(test3)
    log.show_log()
    result4 = test_runner.run(test4)
    log.show_log()

    # Executing the load cell functions and showing the log
    scale = hx711
    loadcell_element = LoadCell()
    loadcell_element.set_scale(scale)
    loadcell_element.tare(scale)
    print("Waterlevel: ",loadcell_element.get_units(scale))
    log.show_log()

    print("|-----------------------------------------|")

    simulator()