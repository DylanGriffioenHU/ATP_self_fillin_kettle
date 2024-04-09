#include "fakeOneWire.cpp"
#include <cstdlib> 

using namespace std; 

// Placeholder for the DallasTemperature library that will be used once the actual DS18B20 sensor is implemented
class DallasTemperature{
    public:
        OneWire oneWire;
        DallasTemperature(OneWire* oneWire){oneWire = oneWire;};
        DallasTemperature(){};

        void begin(){};

        /**
        * Gets the temperature reading from the DS18B20 and returns it (returns a simulated value as the sensor is lacking in this project)
        *
        * @param None
        * @return float returns the temperature the DS18B20 is measuring (returns a simulated value as the sensor is lacking in this project)
        */
        float requestTemperatures(){
            return rand() % 101;
        };
};