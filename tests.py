from util import Pins
import unittest
from waterPumpElement import Pump
from waterHeatingElement import Heating
import logger as log

class Test1_control_heating_element(unittest.TestCase):
    """
    Unit test that tests wether or not the heating element correctly responds to the temperature given in the two scenario's it is required to act on.
    Waterlevel is not used yet in this function so that will always be high enough in this test.
    
    Heating needs to turn on when the temperature is below max_temperature and it needs to turn off once it reaches that temperature or exceeds it    
    """
    def test_heating_element(self):
        relay_pin = Pins.D1
        max_temperature = 100
        min_waterlevel = 1000

        heating_element = Heating()

        heating_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Heat is too low
        heating_element_state = heating_element.control_heat(10, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 1 meaning heating is turned on

        # Heat high enough
        heating_element_state_2 = heating_element.control_heat(100, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off

        self.assertEqual(heating_element_state, 1)
        self.assertEqual(heating_element_state_2, 0)

class Test2_control_pump_element(unittest.TestCase):
    """
    Unit test that tests wether or not the pump element correctly responds to the waterlevel given in the three scenario's it is required to act on.
    
    When the water level is above the minimum but below the maximum the pump needs to turn on
    
    When the waterlevel is at or above the maximum the pump needs to turn of
    
    When the waterlevel is below the minimum it means that the kettle is not on the load cell and the pump cannot turn on
    """
    def test_pump_element(self):
        relay_pin = Pins.D2
        min_waterlevel = 100
        max_waterlevel = 1500

        pump_element = Pump()

        pump_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Waterlevel is too low
        pump_element_state = pump_element.control_pump(200, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 1 meaning pump is turned on

        # Waterlevel high enough
        pump_element_state_2 = pump_element.control_pump(1600, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 0 meaning pump is turned off

        # Waterlevel is below the minimum
        pump_element_state_3 = pump_element.control_pump(0, min_waterlevel, max_waterlevel, relay_pin) # returned state should be 0 meaning pump is turned off

        self.assertEqual(pump_element_state, 1)
        self.assertEqual(pump_element_state_2, 0)
        self.assertEqual(pump_element_state_3, 0)

class Test3_control_heating_element_with_waterlevel(unittest.TestCase):
    """
    Integration test that test wether or not the heating element still works correctly when it also needs to account for the waterlevel
    
    If the heat is too low but the waterlevel is too low the heating element cannot turn on
    
    If heat is high enough but waterlevel is too low then heating element should still be off
    
    (heat doesn't matter if the waterlevel is too low as the heating will always be turned off in that case)
    
    If the heat is too low and the waterlevel is high enough then the heating needs to turn on
    
    If the heat is high enough and the waterlevel is good then the heating should turn off
    """
    def test_heating_with_waterlevel(self):
        relay_pin = Pins.D1
        max_temperature = 100
        min_waterlevel = 1000

        heating_element = Heating()

        heating_element.set_pinmode(relay_pin) # Set the relay pin to output mode

        # Heat is too low, waterlevel is too low
        heating_element_state = heating_element.control_heat(10, max_temperature, 500, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off
        
        # Heat is too low, waterlevel is too low
        heating_element_state_2 = heating_element.control_heat(100, max_temperature, 500, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off

        # Heat high enough, waterlevel is good
        heating_element_state_3 = heating_element.control_heat(10, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 1 meaning heating is turned on

         # Heat high enough, waterlevel is good
        heating_element_state_4 = heating_element.control_heat(100, max_temperature, 1100, min_waterlevel, relay_pin) # returned state should be 0 meaning heating is turned off


        self.assertEqual(heating_element_state, 0)
        self.assertEqual(heating_element_state_2, 0)
        self.assertEqual(heating_element_state_3, 1)
        self.assertEqual(heating_element_state_4, 0)

class Test4_control_heat_and_waterlevel(unittest.TestCase):
    """
    System test that checks all the situations the system can find itself in and makes sure it responds correctly with heat and the pump
    
    Scenario 1 kettle not on load cell - Pump stays turned off and heating stays turned off
    
    Scenario 2 kettle on load cell but empty - Pump turns on but heating stays turned off
    
    Scenario 3 kettle on load cell filled with water but not full yet - Pump stays on and heating turns on
    
    Scenario 4 kettle on load cell fully filled with water - Pump turns off heating stays on
        
    Scenario 5 kettle on load cell fully filled with boiled water - Pump stays off heating turns off
    """
    def test_complete_system(self):
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

    print("|-----------------------------------------|")