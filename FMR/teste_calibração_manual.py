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
#VALOR_PRETO = 5
#VALOR_BRANCO = 95
VALOR_PRETO_ATUAL_D = 0
VALOR_PRETO_ATUAL_E = 0
VALOR_BRANCO_ATUAL_D = 0
VALOR_BRANCO_ATUAL_E = 0
LIMIAR_D = 0
LIMIAR_E = 0
def calibragem():
    global VALOR_BRANCO_ATUAL_D
    global VALOR_BRANCO_ATUAL_E
    global VALOR_PRETO_ATUAL_D
    global VALOR_PRETO_ATUAL_E
    global LIMIAR_D
    global LIMIAR_E
    ev3.screen.draw_text(0, 0, "CALIBRAR PRETO") 
    ev3.screen.draw_text(0, 20, "Centro p/ Continuar")
    while not Button.CENTER in ev3.buttons.pressed():
        wait(10)
    VALOR_PRETO_ATUAL_D = SenseCorD.reflection()
    VALOR_PRETO_ATUAL_E = SenseCorE.reflection()
    #print(f"valor PRETO Direito={VALOR_PRETO_ATUAL_D}")
    #print(f"valor PRETO Esquerdo={VALOR_PRETO_ATUAL_E}")
    wait(1000)
    ev3.screen.clear() 
    ev3.screen.draw_text(0, 0, "CALIBRAR BRANCO")
    ev3.screen.draw_text(0, 20, "Aperte Centro")
    while not Button.CENTER in ev3.buttons.pressed():
        wait(10)
    VALOR_BRANCO_ATUAL_D = SenseCorD.reflection()
    VALOR_BRANCO_ATUAL_E = SenseCorE.reflection()
    #print(f"valor BRANCO Direito={VALOR_BRANCO_ATUAL_D}")
    #print(f"valor BRANCO Esquerdo={VALOR_BRANCO_ATUAL_E}")
    LIMIAR_D = (VALOR_PRETO_ATUAL_D + VALOR_BRANCO_ATUAL_D) / 2
    LIMIAR_E = (VALOR_PRETO_ATUAL_E + VALOR_BRANCO_ATUAL_E) / 2


#Definir Valores para calculo de erro
kp = 3
velo_base = 180
def seguefaixapreta(): #nome autoexplicatico (segue linha)
    #importar variaveis globais
    global Nbifurcaçoes
    global ja_conte_bifurcacao
    global kp
    global velo_base
    global LIMIAR_D
    global LIMIAR_E
    #calculos
    reflexãoEsq = SenseCorE.reflection()
    reflexãoDir = SenseCorD.reflection()
    NORMALIZADO_E = reflexãoEsq-LIMIAR_E
    NORMALIZADO_D = reflexãoDir-LIMIAR_D
    erro = NORMALIZADO_E - NORMALIZADO_D
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
calibragem()
wait(10000)
giroscopio.reset_angle(0)
robot.straight(280)
Stop.HOLD
robot.turn(-78)
Stop.HOLD
robot.stop()
robot.reset()
while True:
    seguefaixapreta()
    if Nbifurcaçoes == 5:
        giro_atual = giroscopio.angle()
        angulo_alvo1 = -89
        angulo_alvo2 = 20
        robot.turn(angulo_alvo1 - giro_atual)
        robot.straight(70)
        Stop.HOLD
        robot.turn(89)
        Stop.HOLD
        robot.straight(195)
        Stop.HOLD
        print(giroscopio.angle())
        robot.turn(angulo_alvo2 - giro_atual)
        CataTampa.run_until_stalled(-200, then=Stop.COAST)
        print("Iniciando missão...")
        wait(800)
        