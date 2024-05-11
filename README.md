# Control your arduino from your PC

The arduino may not have all of the computing power required to do a task. pyduino allows control of your arduino over serial. Note this will replace your entire arduino project.

pyduino is written in python to allow cross-compatibility, such as the popular arudino/pi connection.

# Dependencies

pyduino relies on the __pyserial__ module. This can be installed by running `pip install pyserial` or `sudo pacman -S python-pyserial` on arch-based systems. If pyserial is not installed, the module will try to install it with pip and fail if it is unsuccessfull.

# Getting started

To start create a new `Arduino` instance

```python
import pyduino
with pyduino.Arduino("COM3") as arduino:
    # Do something
```

Signature: `__init__(self, port: str, baudrate: int = 9600)`

**Note:** If you change the baudrate you must also modify `pyduino.ino` to match

After creating the `Arduino` instance, the class exposes the functions found on a normal arduino.

Below are some examples:

```python
import pyduino
with pyduino.Arduino("COM3") as arduino:
    arduino.pinMode(13, pyduino.OUTPUT)
    arduino.digitalWrite(13, True) # This will light up the built-in LED on the UNO
    if arduino.analogRead(0) > 10:
        arduino.digitalWrite(13, False)
```

Signatures:

```python
digitalWrite(self, pin: int, value: bool) -> None
analogWrite(self, pin: int, value: int) -> None
pinMode(self, pin: int, value: int) -> None
digitalRead(self, pin: int) -> bool
analogRead(self, pin: int) -> int
close(self) -> None
```

`pinMode` accepts either 0, 1 or 2 and can be set with the `OUTPUT`, `INPUT` or `INPUT_PULLUP` constants.

Finally, the module exposes the function `parseCommand(pin: int, mod: int) -> bytes` which is meant for internal use only. More information about what it does can be found in the spreadsheet document `Epins.ods`
