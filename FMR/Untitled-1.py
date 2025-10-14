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

#configurações
velocidade_base = 200
limite_preto = 20
limite_branco = 60
bifurcaçoes = 0
birfucações_alvo = 5

def seguir_linha():
    #segue a linha com base na diferença de refletância dos sensores
    ref_esq = SenseCorE.reflection()
    ref_dir = SenseCorD.reflection()
    erro = ref_esq - ref_dir
    ganho = 1.2 #sensibilidade do ajuste 
    RodaEsquerda.dc(velocidade_base - ganho * erro)
    RodaDireita.dc(velocidade_base - ganho * erro)
#loop principal
while True:
    seguir_linha()
    ref_esq = SenseCorE.reflection()
    ref_dir = SenseCorD.reflection()

    #Detectar Bifurcação 
    if ref_esq < limite_preto and ref_dir < limite_preto:
        bifurcaçoes += 1
        ev3.speaker.beep()
        print("Bifurcação detectada:", bifurcaçoes)
        wait(500)

        #virar na 5ª bifurcação
        if bifurcaçoes == 5:
            #Virar à direita
            RodaEsquerda.run_angle(200, 360, Stop.BRAKE, False)
            RodaDireita.run_angle(200, -360, Stop.BRAKE, True)
            break
        #sai do loop principal
while True:
    ref_esq = SenseCorE.reflection()
    ref_dir = SenseCorD.reflection()

    RodaEsquerda.dc(velocidade_base)
    RodaDireita.dc(velocidade_base)

    #parar quando ambos não verem preto
    if ref_esq > limite_branco and ref_dir > limite_branco:
        RodaEsquerda.stop(Stop.BRAKE)
        RodaDireita.stop(Stop.BRAKE)
