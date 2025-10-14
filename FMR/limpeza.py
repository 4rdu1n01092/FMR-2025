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
wait(700)
RodaDireita.stop
RodaEsquerda.stop

while True:
    #PRIMEIRA VOLTA
    robot.turn(55)
    robot.turn(27)
    wait(200)
    robot.stop()
    Print("curva a direita")
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(3000)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)
    Print("andei reto")
    #PRIMEIRA TAMPINHA RIO BAIXO
    robot.turn(46)
    robot.turn(60)
    wait(200)
    robot.stop()
    Print("3 tampa")
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(6500)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    Print("andei mais pra frente")
    #2 TAMPINHAS SEGUIDAS
    robot.turn(-90)
    wait(200)
    robot.stop()
    Print("virei 90 graus")
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(3000)
    RodaDireita.stop
    RodaEsquerda.stop
    Print("mais pra frente dnv")
    wait(200)
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(2000)
    RodaDireita.stop
    RodaEsquerda.stop
    wait(200)
    Print("adivinha? mais frente")
    #ULTIMAS TAMPINHAS
    robot.turn(37)
    wait(200)
    robot.stop()
    Print("virei 37 graus")
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1500)
    RodaEsquerda.stop
    RodaEsquerda.stop
    wait(200)
    Print("mais frente")
    #VOLTA PARA A ESTRADA
    robot.turn(-52)
    wait(400)
    robot.stop()
    Print("girada -52 graus")
    robot.turn(20)
    Print("girada 20 graus")
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1500)
    RodaDireita.stop
    RodaEsquerda.stop
    Print("ultima andada pa frente")
    break
Stop
