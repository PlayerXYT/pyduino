#!/bin/env python3

# Import serial
try:
    import serial, serial.tools.list_ports
except ImportError:
    print("Warning: Module 'serial' not found, attempting install")
    import os
    os.system("pip --isolated -q --no-input --retries 1 install serial")
    try:
        import serial, serial.tools.list_ports

    except ImportError:
        print("Error: Could not import serial, please install it to continue")
        exit()

# Constants
OUTPUT = 0
INPUT = 1
INPUT_PULLUP = 2

HIGH = True
LOW = False

# Arduino wrapper
class Arduino:
    def __init__(self, port: str = None, baudrate: int = 9600):
        if port is None:
            port = search()
        if port is None:
            raise ValueError("Could not find an arduino plugged in")
        self.ser = serial.Serial(port=port, timeout=1)

    def digitalWrite(self, pin: int, value: bool) -> None:
        self.ser.write(parseCommand(pin, 13 if value else 0))

    def analogWrite(self, pin: int, value: int) -> None:
        self.ser.write("{")
        self.ser.write(chr(value+31).encode('ASCII'))

    def pinMode(self, pin: int, value: int) -> None:
        self.ser.write(parseCommand(pin, 26 if value==0 else (39 if value==1 else 52)))

    def digitalRead(self, pin: int) -> bool:
        self.ser.write(parseCommand(pin, 65))
        return self.ser.readlines()[-1].decode("UTF-8").strip()=="1"

    def analogRead(self, pin: int) -> int:
        self.ser.write(parseCommand(pin, 78))
        return int(self.ser.readlines()[-1].decode("UTF-8").strip())

    def close(self) -> None:
        self.ser.close()

# Raw I/O for internal use only
def parseCommand(pin: int, mod: int) -> bytes:
    return chr(pin+mod+31).encode('ASCII')

# Find an arduino by VID
def search() -> str:
    ports = serial.tools.list_ports.comports()
    for i in range(len(ports)):
        if ports[i].vid == 9025:
            return ports[i].device

# If called directly, find arduino
if __name__ == "__main__":
    print(search())
