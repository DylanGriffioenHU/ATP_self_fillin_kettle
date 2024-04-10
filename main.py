from util import Pins
from waterLevelSensor import LoadCell
import logger as log


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