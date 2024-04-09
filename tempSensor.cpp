//#include <OneWire.h>
//#include <DallasTemperature.h>

// Since there won't be an actual sensore in this project fake versions of the library's will be used
// The goal is to replace them with the real library's once the physical sensor is in use without having to change this code
#include "fakeTempSensorLibraries/fakeOneWire.cpp"
#include "fakeTempSensorLibraries/fakeDallasTemperature.cpp"

class DS18B20{
    public:
        #define ONE_WIRE_BUS 22

        OneWire oneWire;
        DallasTemperature sensors;

        DS18B20(){
            // Setup a oneWire instance to communicate with any OneWire devices
            OneWire oneWire(ONE_WIRE_BUS);

            // Pass our oneWire reference to Dallas Temperature sensor 
            DallasTemperature sensors(&oneWire);
        };

        /**
        * Starts up the sensor and makes it ready for temperature reading
        *
        * @param None
        * @return None
        */
        void setup(void)
        {
            sensors.begin();
        }

        /**
        * Gets the temperature reading from the DS18B20 and returns it
        *
        * @param None
        * @return float returns the temperature the DS18B20 is measuring
        */
        float requestTemperature(){
            return sensors.requestTemperatures(); 
        }
};