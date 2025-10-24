#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# === Inicialização ===
ev3 = EV3Brick()
RodaDireita = Motor(Port.B)
RodaEsquerda = Motor(Port.C)
motor_braco = Motor(Port.D)
motor_garra = Motor(Port.A)
sensor_cor = ColorSensor(Port.S2)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=56, axle_track=114)

# === Configurações ===
cores_memorizadas = []
NUM_CORES = 3

# === Funções auxiliares ===
def ler_cor():
    """Lê a cor detectada pelo sensor e retorna o nome."""
    cor = sensor_cor.color()
    if cor == Color.RED:
        print("vermelho")
    elif cor == Color.GREEN:
        print("verde")
    elif cor == Color.BLUE:
        print("azul")
    else:
        return "indefinido"

def mostrar_cor_na_tela(cor_nome):
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Cor: " + cor_nome)
    wait(1000)

def pegar_bolinha():
    motor_braco.run_angle(200, -90, Stop.HOLD)
    motor_garra.run_angle(200, -90, Stop.HOLD)
    wait(500)
    motor_braco.run_angle(200, 90, Stop.HOLD)
    wait(500)

def soltar_bolinha():
    motor_braco.run_angle(200, -90, Stop.HOLD)
    motor_garra.run_angle(200, 90, Stop.HOLD)
    wait(500)
    motor_braco.run_angle(200, 90, Stop.HOLD)

# === Etapa 1: Ler e memorizar 3 cores ===
ev3.speaker.say("Iniciando leitura das cores")
for i in range(NUM_CORES):
    ev3.screen.clear()
    ev3.screen.draw_text(0, 20, "Mostre a cor " + str(i + 1))
    ev3.speaker.beep()
    wait(2000)
    
    cor_atual = ler_cor()
    cores_memorizadas.append(cor_atual)
    mostrar_cor_na_tela(cor_atual)
    ev3.speaker.say("Cor memorizada")

ev3.speaker.say("Todas as cores memorizadas")

# === Etapa 2: Buscar e pegar bolinhas ===
for i in range(NUM_CORES):
    cor_ref = cores_memorizadas[i]
    ev3.speaker.say("Buscando " + cor_ref)

    while True:
        cor_lida = ler_cor()
        if cor_lida == cor_ref:
            ev3.speaker.say("Cor encontrada")
            robot.stop()
            pegar_bolinha()
            break
        else:
            robot.drive(50, 10)

    robot.straight(100)
    soltar_bolinha()
    robot.straight(-100)

ev3.speaker.say("Tarefa concluída")
robot.stop()
