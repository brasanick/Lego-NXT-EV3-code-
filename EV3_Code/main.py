#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Objective: The robot follows a line using two color sensors. 
# It avoids obstacles using an ultrasonic sensor.


# Objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
front_motor = Motor(Port.C)
back_motor = Motor(Port.D)
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S2)
ultra_sensor = UltrasonicSensor(Port.S3)
infra_sensor = InfraredSensor(Port.S4)
near = 200  # Distance in mm
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)



def map_road():
    robot.drive(200, 0)

def catch():
    front_motor.run_angle(200, 90)
    wait(1500)
    front_motor.run_angle(200, -90)

def stop_robot():
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

def avoid_obstacle():
    while ultra_sensor.distance() < near:
        robot.straight(-60)

    robot.turn(90)
    robot.straight(200)
    robot.turn(-90)
    robot.straight(100)
    robot.turn(-90)
    robot.straight(100)


while True:

    if ultra_sensor.distance() > near:
        if color1.color() == Color.BLACK and color2.color() == Color.BLACK:
            robot.drive(200, 0)

        elif color1.color() == Color.BLACK and color2.color() == Color.WHITE:
            robot.turn(90)

        elif color1.color() == Color.WHITE and color2.color() == Color.BLACK:
            robot.turn(-90)

        elif color1.color() == Color.WHITE and color2.color() == Color.WHITE:
            robot.drive(200, 0)

        elif color1.color() == Color.GREEN and color2.color() == Color.GREEN:
            robot.turn(180)

        elif color1.color() == Color.GREEN and color2.color() == Color.WHITE:
            robot.turn(90)

        elif color1.color() == Color.WHITE and color2.color() == Color.GREEN:
            robot.turn(-90)

        elif color1.color() == Color.RED and color2.color() == Color.RED:
            stop_robot()
            ev3.speaker.beep()

    else:
        avoid_obstacle()































    #---------------------------------------------

    ev3 = EV3Brick()

# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacle_sensor = UltrasonicSensor(Port.S4)

# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
# The axle track is the distance between the points where the wheels
# touch the ground.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()

# The following loop makes the robot drive forward until it detects an
# obstacle. Then it backs up and turns around. It keeps on doing this
# until you stop the program.
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance() > 300:
        wait(10)

    # Drive backward for 300 millimeters.
    robot.straight(-300)

    # Turn around by 120 degrees
    robot.turn(120)
