#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

chasis = DriveBase(left_motor, right_motor, wheel_diameter=44, axle_track=130)

# Write your program here.
ev3.speaker.beep()
chasis.straight(270)
chasis.turn(90)
chasis.straight(240)
chasis.turn(-90)
chasis.straight(600)
chasis.turn(-166)
chasis.straight(460)
chasis.turn(*90)
chasis.straight(140)
chasis.turn(90)
chasis.straight(140)