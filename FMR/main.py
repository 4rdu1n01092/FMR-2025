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
estounopontodepartida = True
if estounopontodepartida == True:
    RodaEsquerda.run(1000)
    RodaDireita.run(1000)
    estounopontodepartida = False
#variaveis
Nbifurcaçoes = 0
ja_conte_bifurcacao = False
def seguefaixapreta(): #nome autoexplicatico (segue linha)
    #importar variaveis globais
    global Nbifurcaçoes
    global ja_conte_bifurcacao
    #Definir Valores para calculo de erro
    kp = 3
    velo_base = 200
    #calculos
    reflexãoEsq = SenseCorE.reflection()
    reflexãoDir = SenseCorD.reflection()
    erro = reflexãoEsq - reflexãoDir
    correçao = kp * erro
    RodaDireita.run(velo_base-correçao)
    RodaEsquerda.run(velo_base+correçao)
    #detectar Birfuca
    if estounopontodepartida == False:
        if reflexãoEsq <= 50 and reflexãoDir <= 50 and not ja_conte_bifurcacao:
            Nbifurcaçoes += 1
            print(Nbifurcaçoes)
            ja_conte_bifurcacao = True
            RodaDireita.run_time(500, 200, wait=False) 
            RodaEsquerda.run_time(500, 200, wait=True) 
        elif reflexãoEsq >= 70 and reflexãoDir >= 70 and ja_conte_bifurcacao:
            ja_conte_bifurcacao = False

#Sequencia do programa
MotorGarraBaixo.run_until_stalled(-100, then=Stop.BRAKE, duty_limit=None)

while True:   


    seguefaixapreta()
    if Nbifurcaçoes == 5:
        robot.straight(60)
        robot.turn(120)
        robot.stop()
        cronometro = StopWatch()
        cronometro.reset() 
        while cronometro.time() < 1000:
            seguefaixapreta()
        RodaDireita.stop() 
        RodaEsquerda.stop()
        break

Stop
