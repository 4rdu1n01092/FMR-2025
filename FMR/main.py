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
kp = 3
velo_base = 180
#Funçoes do programa
def seguir_até_a_misão_de_coletar_as_tampinhas():
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
#Sequencia inicial do programa
def sequencia_inicial():
    giroscopio.reset_angle(0)
    robot.straight(280)
    Stop.HOLD
    robot.turn(-78)
    Stop.HOLD
    robot.stop()
    robot.reset()
# seguir faixa preta
def segue_faixa_preta(): 
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
#inicio missão
def inicio_missão():
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(700)
    RodaDireita.stop
    RodaEsquerda.stop
#PRIMEIRA VOLTA
def primeira_volta():
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
def primeira_tampinha_rio_baixo():
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
def tampinha_seguidas():
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
def ultimas_tampinhas():
    robot.turn(35)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1600)
    RodaEsquerda.stop
    RodaEsquerda.stop
    wait(200)
#VOLTA PARA A ESTRADA
def volta_para_a_estrada_pós_missão_tampinhas():
    robot.turn(-34)
    wait(400)
    robot.stop()
    robot.turn(0)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1800)
    RodaDireita.stop
    RodaEsquerda.stop
#parar robo
def parar_robo():
    RodaDireita.stop()
    RodaEsquerda.stop()
# missão tampinhas
def missão_tampinhas():
    inicio_missão()
    primeira_volta()
    primeira_tampinha_rio_baixo()
    tampinha_seguidas()
    ultimas_tampinhas()
    volta_para_a_estrada_pós_missão_tampinhas()
    parar_robo()

#Sequencia do programa
sequencia_inicial()
while True:
    segue_faixa_preta()
    if Nbifurcaçoes == 5:
        parar_robo()
        seguir_até_a_misão_de_coletar_as_tampinhas()
        wait(5000)
        missão_tampinhas()
