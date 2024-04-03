#include "fakeOneWire.cpp"
#include <cstdlib> 

using namespace std; 

class DallasTemperature{
    public:
        OneWire oneWire;
        DallasTemperature(OneWire* oneWire){oneWire = oneWire;};
        DallasTemperature(){};

        void begin(){};

        float requestTemperatures(){
            return rand() % 101;
        };
};