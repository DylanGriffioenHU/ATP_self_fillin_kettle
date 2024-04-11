from util import Pins
from waterLevelSensor import LoadCell
from waterPumpElement import Pump
from waterHeatingElement import Heating
import logger as log
import unittest

class Test1_control_heating_element(unittest.TestCase):
    def test_open_gate(self):
        heating_element = Heating(100,1000, Pins.D1)

        # Heat is too low, waterlevel is good and heating element is not on
        heating_element_state = heating_element.control_heat(10, 1100, 0) # returned state should be 1 meaning heating is turned on

        # Heat high enough, waterlevel is good and heating element is on
        heating_element_state_2 = heating_element.control_heat(100, 1100, 1) # returned state should be 0 meaning heating is turned off

        self.assertEqual(heating_element_state, 1)
        self.assertEqual(heating_element_state_2, 0)

class Test2_control_pump_element(unittest.TestCase):
    def test_open_gate(self):
        pump_element = Pump(100,1500, Pins.D2)

        # Waterlevel is too low and pump element is not on
        pump_element_state = pump_element.control_pump(200, 0) # returned state should be 1 meaning pump is turned on

        # Waterlevel high enough and pump element is on
        pump_element_state_2 = pump_element.control_pump(1600, 1) # returned state should be 0 meaning pump is turned off

        # Waterlevel high enough and pump element is on
        pump_element_state_3 = pump_element.control_pump(0, 1) # returned state should be 0 meaning pump is turned off

        self.assertEqual(pump_element_state, 1)
        self.assertEqual(pump_element_state_2, 0)
        self.assertEqual(pump_element_state_3, 0)

class Test3_control_heating_element_with_waterlevel(unittest.TestCase):
    def test_open_gate(self):
        heating_element = Heating(100,1000, Pins.D1)

        # Heat is too low, waterlevel is good and heating element is not on
        heating_element_state = heating_element.control_heat(10, 500, 1) # returned state should be 1 meaning heating is turned on

        # Heat is too low, waterlevel is good and heating element is not on
        heating_element_state_2 = heating_element.control_heat(10, 1100, 0) # returned state should be 1 meaning heating is turned on

        # Heat high enough, waterlevel is good and heating element is on
        heating_element_state_3 = heating_element.control_heat(100, 1100, 1) # returned state should be 0 meaning heating is turned off

        self.assertEqual(heating_element_state, 0)
        self.assertEqual(heating_element_state_2, 1)
        self.assertEqual(heating_element_state_3, 0)

if __name__ == '__main__':
    log.show_log()
    loadcell = LoadCell()
    print(loadcell.get_units())
    log.show_log()
    #print(loadcell.get_units())
    #print(loadcell.get_units())
    log.show_log()
    ONE_WIRE_BUS = 4
    print("One wire bus: ",ONE_WIRE_BUS)
    print("Pin: ",Pins.D2.value)

    test_loader = unittest.TestLoader()
    test1 = test_loader.loadTestsFromTestCase(Test1_control_heating_element)
    test2 = test_loader.loadTestsFromTestCase(Test2_control_pump_element)
    test3 = test_loader.loadTestsFromTestCase(Test3_control_heating_element_with_waterlevel)

    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test1)
    log.show_log()

    result2 = test_runner.run(test2)
    log.show_log()

    result3 = test_runner.run(test3)
    log.show_log()