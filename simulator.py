from util import Pins
from waterPumpElement import Pump
from waterHeatingElement import Heating
import time

def simulator(auto = False, sleep = 1):
    relay_pin_1 = Pins.D1
    relay_pin_2 = Pins.D2
    min_waterlevel_pump = 100
    min_waterlevel_heat = 1000
    max_waterlevel = 1500
    max_temperature = 100

    # Scenario 1 kettle not on load cell
    water_level = 0
    temperature = 0

    heating_element = Heating()
    pump_element = Pump()

    heating_element.set_pinmode(relay_pin_1) # Set the relay pin to output mode
    pump_element.set_pinmode(relay_pin_2) # Set the relay pin to output mode
    print()

    while(True):
        heating_element_state = heating_element.control_heat(temperature, max_temperature, water_level, min_waterlevel_heat, relay_pin_1)
        print()
        if heating_element_state:
            print("Heating is turned on")
        else:
            print("Heating is turned off")
        print()

        pump_element_state = pump_element.control_pump(water_level, min_waterlevel_pump, max_waterlevel, relay_pin_2)
        print()
        if pump_element_state:
            print("Pump is turned on")
        else:
            print("Pump is turned off")
        print()

        if pump_element_state:
            water_level += 100

        if heating_element_state:
            temperature += 10
        
        print("Water level: ", water_level)
        print("Water temperature: ", temperature)
        print()
        
        if water_level < min_waterlevel_pump:
            if auto:
                print("Press y to put the kettle on the load cell")
                print()
                user_input = input()
                if user_input == "y":
                    water_level = min_waterlevel_pump
            else:
                print("putting kettle on load cell to fill with and boil water")
                print()
                water_level = min_waterlevel_pump
    
        if temperature == max_temperature:
            if auto:
                print("press y to remove the kettle from the load cell and take your boiling water")
                print("press n to quit the simulation")
                print()
                user_input = input()
                if user_input == "y":
                    water_level = 0
                    temperature = 0
                elif user_input == "n":
                    break
            else:
                print("removing kettle from load cell to set tea")
                print()
                water_level = 0
                temperature = 0

        print("|-----------------------------------------|")
        time.sleep(sleep)
        
    return