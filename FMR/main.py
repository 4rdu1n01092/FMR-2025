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
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
# Definir blocos EV3 e motores
ev3 = EV3Brick()
RodaDireita = Motor(Port.B)
RodaEsquerda = Motor(Port.C)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)
#missoes 
def limpezaRio():
    print("executando percurso e coletando lixo")
    RodaDireita.run(3.5)
#sequencia de inicializacao
def Iniciar():
    for i in range(3):
        ev3.screen.print("Inicializando")
        ev3.screen.clear()
        wait(1000)
        ev3.screen.print("Inicializando.")
        ev3.screen.clear()
        wait(1000)
        ev3.screen.print("Inicializando..")
        ev3.screen.clear()
        wait(1000)
        ev3.screen.print("Inicializando...")
        ev3.screen.clear()
        wait(1000)
    ev3.screen.print("Pronto!")
    wait(1000)
    ev3.screen.clear() 

#Sequencia do programa
Iniciar()
print("Programa sendo iniciado")

wait(13000)
print("Programa Iniciado com sucesso!")
print("Limpando rio...")
limpezaRio()
wait(50000)
print("Limpeza concluida ✔️")
wait(5)
