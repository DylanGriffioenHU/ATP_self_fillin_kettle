# Fake arduino library to simulate using the real one
def pinMode(relayPin, OUTPUT) -> None:
    pass

def digitalWrite(relayPin, HIGH) -> None:
    pass

HIGH = 1
LOW = 0
OUTPUT = "OUTPUT"