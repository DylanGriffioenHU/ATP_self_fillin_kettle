from util import Pins
import unittest
from waterPumpElement import Pump
from waterHeatingElement import Heating

class Test1_control_heating_element(unittest.TestCase):
    def test_open_gate(self):
        relay_pin = Pins.D1
        max_temperature = 100
        min_waterlevel = 1000

        heating_element = Heating()

        heating_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Heat is too low, waterlevel is good and heating element is not on
        heating_element_state = heating_element.control_heat(10, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 1 meaning heating is turned on

        # Heat high enough, waterlevel is good and heating element is on
        heating_element_state_2 = heating_element.control_heat(100, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off

        self.assertEqual(heating_element_state, 1)
        self.assertEqual(heating_element_state_2, 0)

class Test2_control_pump_element(unittest.TestCase):
    def test_open_gate(self):
        relay_pin = Pins.D2
        min_waterlevel = 100
        max_waterlevel = 1500

        pump_element = Pump()

        pump_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Waterlevel is too low and pump element is not on
        pump_element_state = pump_element.control_pump(200, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 1 meaning pump is turned on

        # Waterlevel high enough and pump element is on
        pump_element_state_2 = pump_element.control_pump(1600, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 0 meaning pump is turned off

        # Waterlevel high enough and pump element is on
        pump_element_state_3 = pump_element.control_pump(0, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 0 meaning pump is turned off

        self.assertEqual(pump_element_state, 1)
        self.assertEqual(pump_element_state_2, 0)
        self.assertEqual(pump_element_state_3, 0)

class Test3_control_heating_element_with_waterlevel(unittest.TestCase):
    def test_open_gate(self):
        relay_pin = Pins.D1
        max_temperature = 100
        min_waterlevel = 1000

        heating_element = Heating()

        heating_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Heat is too low, waterlevel is good and heating element is not on
        heating_element_state = heating_element.control_heat(10, max_temperature, 500, min_waterlevel, relay_pin) # returned state should be 1 meaning heating is turned on

        # Heat high enough, waterlevel is good and heating element is on
        heating_element_state_2 = heating_element.control_heat(10, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off

         # Heat high enough, waterlevel is good and heating element is on
        heating_element_state_3 = heating_element.control_heat(100, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off


        self.assertEqual(heating_element_state, 0)
        self.assertEqual(heating_element_state_2, 1)
        self.assertEqual(heating_element_state_3, 0)

class Test4_control_heat_and_waterlevel(unittest.TestCase):
    def test_open_gate(self):
        relay_pin_1 = Pins.D1
        relay_pin_2 = Pins.D2
        min_waterlevel_pump = 100
        min_waterlevel_heat = 1000
        max_waterlevel = 1500
        max_temperature = 100

        # Scenario 1 kettle not on load cell
        water_level = 10
        temperature = 5

        heating_element = Heating()
        pump_element = Pump()

        heating_element.set_pinmode(relay_pin_1) # Set the relay pin to output mode
        pump_element.set_pinmode(relay_pin_2) # Set the relay pin to output mode

        # Pump stays turned off and heating stays turned off
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)

        self.assertEqual(heating_element_state, 0)
        self.assertEqual(pump_element_state, 0)

        # Scenario 2 kettle on load cell but empty
        water_level = 200
        temperature = 5

        # Pump turns on but heating stays turned off
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)

        self.assertEqual(heating_element_state, 0)
        self.assertEqual(pump_element_state, 1)

        # Scenario 3 kettle on load cell filled with water but not full yet
        water_level = 1100
        temperature = 5

        # Pump stays on and heating turns on
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)

        self.assertEqual(heating_element_state, 1)
        self.assertEqual(pump_element_state, 1)

        # Scenario 4 kettle on load cell fully filled with water
        water_level = 1600
        temperature = 5

        # Pump turns off heating stays on
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)

        self.assertEqual(heating_element_state, 1)
        self.assertEqual(pump_element_state, 0)

        # Scenario 5 kettle on load cell fully filled with boiled water
        water_level = 1600
        temperature = 100

        # Pump stays off heating turns off
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)

        self.assertEqual(heating_element_state, 0)
        self.assertEqual(pump_element_state, 0)