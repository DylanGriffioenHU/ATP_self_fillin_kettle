#ifdef _MSC_VER
    #define EXPORT_SYMBOL __declspec(dllexport)
#else
    #define EXPORT_SYMBOL
#endif

#ifdef __cplusplus
extern "C" {
#endif

EXPORT_SYMBOL float request_temperature_from_sensor(int ONE_WIRE_BUS);

#ifdef __cplusplus
}
#endif

