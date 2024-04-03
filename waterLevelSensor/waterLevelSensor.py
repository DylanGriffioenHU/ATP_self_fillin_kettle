#include "HX711.h"
from util import Pins
from fakehx711 import hx711

class loadCell:
    def __init__(self):
        # HX711 circuit wiring
        LOADCELL_DOUT_PIN = Pins.D23;
        LOADCELL_SCK_PIN = Pins.D24;
        self.scale = hx711
        pass

    def setup(self):
        pass
    
    def setScale():
        scale.set_scale()



#HX711 scale;

