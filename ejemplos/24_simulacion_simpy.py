# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install simpy
# 2. Ejecuta el script: python 24_simulacion_simpy.py

import simpy
import random

class Parada:
    def __init__(self, env, capacidad_bus):
        self.personas = 0
        self.env = env
        self.capacidad_bus = capacidad_bus

    def llega_persona(self):
        while True:
            llegan = random.randint(0, 10)
            print(f"[PERSONA] Llegan {llegan} en el minuto {self.env.now}")
            self.personas += llegan
            yield self.env.timeout(1)

    def llega_bus(self):
        while True:
            se_lleva = min(self.capacidad_bus, self.personas)
            self.personas -= se_lleva
            print(f"[BUS] Se lleva: {se_lleva} y quedan {self.personas}")
            yield self.env.timeout(random.uniform(5, 10))

env = simpy.Environment()
parada = Parada(env, capacidad_bus=50)

env.process(parada.llega_persona())
env.process(parada.llega_bus())
env.run(until=120)