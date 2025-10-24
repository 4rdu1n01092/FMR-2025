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
motor_braco = Motor(Port.D)
motor_garra = Motor(Port.A)
sensor_cor = ColorSensor(Port.S2)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)

#Funções auxiliares 
def mover_braco(angulo, velocidade=200):
    "Move o braço (e o sensor de cor) para cima ou para baixo."
    motor_braco.run_angle(velocidade,angulo, Stop.BRAKE, True)

def ler_cor():
    "Lê a cor atual do sensor."
    cor = sensor_cor.color()
    if cor == Color.RED:
        return "Vermelho"
    elif cor == Color.BLUE:
        return "Azul"
    elif cor == Color.GREEN:
        return "Verde"
    else:
        return "desconhecido"
    
def abrir_guarra():
    motor_garra.run_angle(200, 120, Stop.BRAKE, True)

def fechar_garra():
    motor_garra.run_angle(200, -120, Stop.BRAKE, True)

ev3.speaker.say("Iniciando leitura das cores")
cores_memorizadas = []

#O braço começa em cima e desce de forma gradual lendo as 3 cores
for i in range (3):
    mover_braco(-200, 200) #desce um pouco
    wait(500)
    cor_detectada = ler_cor()

    cores_memorizadas.append(cor_detectada)
    ev3.speaker.say(cor_detectada)
    #print(f"Cor detectada {i+1}:{cor_detectada}")
    wait(500)

#sobe o braço de volta à posição inicial
mover_braco(600, 200)
ev3.speaker.beep()
print("Sequencia decorada(de baixo para cima):", cores_memorizadas)

#agora o robô vai pegar as bolinhas nessa ordem
ev3.speaker.say("Pegando as bolinhas")

for cor in cores_memorizadas:
    ev3.speaker.say(f"Pegar {cor}")
    print(f"Pegar bolinha {cor}")

    # Aqui você pode colocar lágica diferente para cada cor, se quiser
    # Mas como as bolinhas estão juntas na caixa, ele só precisa fazer a sequência

    abrir_guarra()
    wait(300)
    fechar_garra()
    wait(1000)

    #Após pegar uma bolinha, ele pode "soltar" em outro local ou só simular a ação
    abrir_guarra()
    wait(500)

ev3.speaker.say ("Sequência completa")
ev3.speaker.beep()
print("Todas as bolinhas foram pegas na ordem certa")