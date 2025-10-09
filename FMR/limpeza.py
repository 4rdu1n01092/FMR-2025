#!/usr/bin/env pybricks-micropython
# Importar bibliotecas necessárias do Pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Definir blocos EV3 e motores
ev3 = EV3Brick()
RodaDireita = Motor(Port.B)
RodaEsquerda = Motor(Port.C)
MotorGarraBaixo = Motor(Port.D)
MotorGarraAlta = Motor(Port.A)
SenseCorD = ColorSensor(Port.S1)
SenseCorE = ColorSensor(Port.S4)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
#missoes 

RodaDireita.run(200)
RodaEsquerda.run(200)
wait(500)
RodaDireita.stop
RodaEsquerda.stop
RodaDireita.run(200)
RodaEsquerda.run(200)
wait(1000)
RodaDireita.stop
RodaEsquerda.stop

while True:
    robot.turn(60)
    robot.turn(55)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(3000)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    robot.turn(50)
    robot.turn(58)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(6000)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    robot.turn(-78)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(3000)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    robot.turn(-50)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(2500)
    RodaDireita.stop
    RodaEsquerda.stop






