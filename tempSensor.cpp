//#include <OneWire.h>
//#include <DallasTemperature.h>

// Since there won't be an actual sensore in this project fake versions of the library's will be used
// The goal is to replace them with the real library's once the physical sensor is in use without having to change this code
#include "fakeTempSensorLibraries/fakeOneWire.cpp"
#include "fakeTempSensorLibraries/fakeDallasTemperature.cpp"

class DS18B20{
    public:
        DS18B20(){};

        /**
        * Starts up the sensor and makes it ready for temperature reading
        *
        * @param None
        * @return None
        */
        void setup(DallasTemperature sensors){
            sensors.begin();
        }

        /**
        * Gets the temperature reading from the DS18B20 and returns it
        *
        * @param None
        * @return float returns the temperature the DS18B20 is measuring
        */
        float request_temperature(DallasTemperature sensors){
            return sensors.requestTemperatures(); 
        }
};

/**
* Creates a DS18B20 object, sets it up and returns a temperature reading.
*
* @param int: ONE_WIRE_BUS the pin number that the one wire bus is meant to be created on
* @return float returns the temperature the DS18B20 is measuring
*/
float request_temperature_from_sensor(int ONE_WIRE_BUS){
    // Setup a oneWire instance to communicate with any OneWire devices
    OneWire oneWire(ONE_WIRE_BUS);

    // Pass our oneWire reference to Dallas Temperature sensor 
    DallasTemperature sensors(&oneWire);

    DS18B20 temp_sensor;

    temp_sensor.setup(sensors);

    return temp_sensor.request_temperature(sensors);
}
