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
CataTampa = Motor(Port.D)
MotorGarraAlta = Motor(Port.A)
SenseCorD = ColorSensor(Port.S3)
SenseCorE = ColorSensor(Port.S4)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
giroscopio = GyroSensor(Port.S2)
#missoes 

RodaDireita.run(200)
RodaEsquerda.run(200)
wait(700)
RodaDireita.stop
RodaEsquerda.stop

while True:
    #PRIMEIRA VOLTA
    robot.turn(50)
    robot.turn(38)
    wait(200)
    robot.stop()
    RodaDireita.run(170)
    RodaEsquerda.run(170)
    wait(3000)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)
    #PRIMEIRA TAMPINHA RIO BAIXO
    robot.turn(50)
    robot.turn(45)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(6500)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)

    #2 TAMPINHAS SEGUIDAS
    robot.turn(-85)
    wait(200)
    robot.stop()
    RodaDireita.run(220)
    RodaEsquerda.run(220)
    wait(3500)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1750)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    #ULTIMAS TAMPINHAS
    robot.turn(35)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1700)
    RodaEsquerda.stop
    RodaEsquerda.stop
    wait(200)
    #VOLTA PARA A ESTRADA
    robot.turn(-34)
    wait(400)
    robot.stop()
    robot.turn(0)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1500)
    RodaDireita.stop
    RodaEsquerda.stop
    break
RodaDireita.stop(Stop.BRAKE)
RodaEsquerda.stop(Stop.BRAKE)
Stop
