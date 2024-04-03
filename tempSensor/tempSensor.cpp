//#include <OneWire.h>
//#include <DallasTemperature.h>

// Since there won't be an actual sensore in this project fake versions of the library's will be used
// The goal is to replace them with the real library's once the physical sensor is in use without having to change this code
#include "fakeOneWire.cpp"
#include "fakeDallasTemperature.cpp"

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

        void setup(void)
        {
            //Start up the library
            sensors.begin();
        }

        float requestTemperature(){
            return sensors.requestTemperatures(); 
        }
};