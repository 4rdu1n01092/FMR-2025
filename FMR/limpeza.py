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
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
#missoes 

print("executando percurso e coletando lixo")
robot.straight(88)
robot.turn(75)
robot.straight(330)
wait(20)
robot.turn(65)
robot.straight(100)
robot.turn(27)
robot.straight(90)
robot.turn(-25)
robot.straight(90) 
robot.turn(80)
robot.straight(410)
robot.turn(-35)
robot.straight(40)

