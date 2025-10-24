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

# variaveis
Nbifurcaçoes = 0
ja_conte_bifurcacao = False
VALOR_PRETO = 5
VALOR_BRANCO = 95
kp = 1.8
velo_base = 180

# === Funções auxiliares ===
def girar_para(angulo_alvo):
    """Gira o robô até o ângulo absoluto desejado com base no giroscópio."""
    robot.turn(angulo_alvo)
    robot.stop()

def ir_para_frente(distancia):
    """Move o robô para frente (ou trás se valor negativo) em milímetros."""
    robot.straight(distancia)
    robot.stop()

# === Função atualizada: seguir até a missão das tampinhas ===
def seguir_até_a_misão_de_coletar_as_tampinhas():
    ir_para_frente(70)
    girar_para(90)
    ir_para_frente(195)
    CataTampa.run_until_stalled(-200, then=Stop.COAST)
    print("Iniciando missão...")
    wait(800)

# Sequencia inicial do programa
def sequencia_inicial():
    giroscopio.reset_angle(0)
    robot.straight(280)
    robot.stop()
    robot.turn(-78)
    robot.stop()
    robot.stop()  # garantia
    robot.reset()

# seguir faixa preta
def segue_faixa_preta():
    global Nbifurcaçoes
    global ja_conte_bifurcacao
    global kp
    global velo_base
    # leitura dos sensores
    reflexaoEsq = SenseCorE.reflection()
    reflexaoDir = SenseCorD.reflection()
    erro = reflexaoEsq - reflexaoDir
    correcao = kp * erro
    # ajustar velocidade dos motores (atenção: .run espera valores em deg/s)
    RodaDireita.run(velo_base - correcao)
    RodaEsquerda.run(velo_base + correcao)
    # detectar bifurcação (valores podem precisar de afinação conforme pista)
    if reflexaoEsq <= 50 and reflexaoDir <= 50 and not ja_conte_bifurcacao:
        Nbifurcaçoes += 1
        print("Bifurcação detectada. Total:", Nbifurcaçoes)
        ja_conte_bifurcacao = True
        # pequeno impulso para frente (200 ms a 500 deg/s)
        RodaDireita.run_time(500, 200, wait=False)
        RodaEsquerda.run_time(500, 200, wait=True)
    elif reflexaoEsq >= 60 and reflexaoDir >= 60 and ja_conte_bifurcacao:
        ja_conte_bifurcacao = False

# inicio missão
def inicio_missão():
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(700)
    RodaDireita.stop()
    RodaEsquerda.stop()

# PRIMEIRA VOLTA
def primeira_volta():
    robot.turn(70)
    wait(200)
    robot.stop()
    RodaDireita.run(170)
    RodaEsquerda.run(170)
    wait(3000)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)

# PRIMEIRA TAMPINHA RIO BAIXO
def primeira_tampinha_rio_baixo():
    robot.turn(50)
    robot.turn(45)
    wait(200)
    robot.stop()
    RodaDireita.run(220)
    RodaEsquerda.run(220)
    wait(6500)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)

# 2 TAMPINHAS SEGUIDAS
def tampinha_seguidas():
    robot.turn(-85)
    wait(200)
    robot.stop()
    RodaDireita.run(220)
    RodaEsquerda.run(220)
    wait(3500)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)
    RodaDireita.run(250)
    RodaEsquerda.run(250)
    wait(1750)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)

# ULTIMAS TAMPINHAS
def ultimas_tampinhas():
    robot.turn(35)
    wait(200)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1600)
    RodaDireita.stop()
    RodaEsquerda.stop()
    wait(200)

# VOLTA PARA A ESTRADA
def volta_para_a_estrada_pós_missão_tampinhas():
    robot.turn(-34)
    wait(400)
    robot.stop()
    RodaDireita.run(200)
    RodaEsquerda.run(200)
    wait(1800)
    RodaDireita.stop()
    RodaEsquerda.stop()

# parar robo
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

# Sequencia do programa
sequencia_inicial()
while True:
    segue_faixa_preta()
    if Nbifurcaçoes == 5:
        parar_robo()
        seguir_até_a_misão_de_coletar_as_tampinhas()
        wait(5000)
        missão_tampinhas()
        break
