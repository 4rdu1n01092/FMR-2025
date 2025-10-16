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
#variaveis
Nbifurcaçoes = 0
ja_conte_bifurcacao = False
VALOR_PRETO = 5
VALOR_BRANCO = 95
#Definir Valores para calculo de erro
kp = 3
velo_base = 180
def seguefaixapreta(): #nome autoexplicatico (segue linha)
    #importar variaveis globais
    global Nbifurcaçoes
    global ja_conte_bifurcacao
    global kp
    global velo_base
    #calculos
    reflexãoEsq = SenseCorE.reflection()
    reflexãoDir = SenseCorD.reflection()
    erro = reflexãoEsq - reflexãoDir
    correçao = kp * erro
    RodaDireita.run(velo_base-correçao)
    RodaEsquerda.run(velo_base+correçao)
    #detectar Birfuca
    if reflexãoEsq <= 50 and reflexãoDir <= 50 and not ja_conte_bifurcacao:
        Nbifurcaçoes += 1
        print(Nbifurcaçoes)
        ja_conte_bifurcacao = True
        RodaDireita.run_time(500, 200, wait=False) 
        RodaEsquerda.run_time(500, 200, wait=True) 
    elif reflexãoEsq >= 60 and reflexãoDir >= 60 and ja_conte_bifurcacao:
        ja_conte_bifurcacao = False
#Sequencia do programa
robot.straight(280)
robot.turn(-76)
robot.stop()
while True:
    seguefaixapreta()
    if Nbifurcaçoes == 5:
        while giroscopio.angle() != -82:
            robot.turn(-1)  
        robot.straight(70)
        robot.turn(95)
        robot.straight(200)
        CataTampa.run_until_stalled(-200, then=Stop.COAST)
        print("Iniciando missão...")
        wait(800)
        