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
SensorCorVermelhoCima = ColorSensor(Port.S1)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
#missoes
def limpezario():
    RodaDireita.run(200)
    RodaEsquerda.run(400)
    wait(500)
    RodaDireita.stop
    RodaEsquerda.stop
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1000)
    RodaDireita.stop
    RodaEsquerda.stop
    while True:
        robot.turn(50)
        robot.turn(42)
        wait(200)
        robot.stop()
        RodaDireita.run(200)
        RodaEsquerda.run(200)
        wait(3000)
        RodaDireita.stop
        RodaEsquerda.stop
        wait(200)
        robot.turn(50)
        robot.turn(48)
        wait(200)
        robot.stop()
        RodaDireita.run(200)
        RodaEsquerda.run(200)
        wait(7000)
        RodaDireita.stop
        RodaEsquerda.stop
        wait(200)
        robot.turn(-65)
        wait(200)
        robot.stop()
        RodaDireita.run(200)
        RodaEsquerda.run(200)
        wait(3000)
        RodaDireita.stop
        RodaEsquerda.stop
        wait(200)
        robot.turn(-10)
        wait(200)
        robot.stop()
        RodaDireita.run(200)
        RodaEsquerda.run(200)
        wait(2500)
        RodaDireita.stop
        RodaEsquerda.stop
#variaveis
Nbifurcaçoes = -1
ja_conte_bifurcacao = False
def seguefaixapreta(): #nome autoexplicatico (segue linha)
    #importar variaveis globais
    global Nbifurcaçoes
    global ja_conte_bifurcacao
    #Definir Valores para calculo de erro
    kp = 3.5
    velo_base = 180
    #calculos
    reflexãoEsq = SenseCorE.reflection()
    reflexãoDir = SenseCorD.reflection()
    erro = reflexãoEsq - reflexãoDir
    correçao = kp * erro
    RodaDireita.run(velo_base-correçao)
    RodaEsquerda.run(velo_base+correçao)
    #detectar Birfuca
    if reflexãoEsq <= 49 and reflexãoDir <= 49 and not ja_conte_bifurcacao:
        Nbifurcaçoes += 1
        print(Nbifurcaçoes)
        ja_conte_bifurcacao = True
        RodaDireita.run_time(500, 200, wait=False) 
        RodaEsquerda.run_time(500, 200, wait=True) 
    elif reflexãoEsq >= 50 and reflexãoDir >= 50 and ja_conte_bifurcacao:
        ja_conte_bifurcacao = False
#Sequencia do programa
RodaDireita.run(200)
RodaEsquerda.run(400)
wait(500)
RodaDireita.stop
RodaEsquerda.stop
RodaDireita.run(200)
RodaEsquerda.run(200)
wait(1000)
RodaDireita.stop
RodaEsquerda.stop
while True:    
    seguefaixapreta()
    if Nbifurcaçoes == 5:
        robot.straight(60)
        robot.turn(87)
        robot.stop()
        cronometro = StopWatch()
        cronometro.reset() 
        while cronometro.time() < 3000:
            seguefaixapreta()
        RodaDireita.stop() 
        RodaEsquerda.stop()
        CataTampa.run_until_stalled(-2000, then=Stop.COAST, duty_limit=None)
        break
Stop