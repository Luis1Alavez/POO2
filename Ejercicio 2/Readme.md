# 💰 Ejercicio de Programación Orientada a Objetos (POO)
## Sistema de Cuenta Bancaria

### 📌 Descripción

Este ejercicio consiste en desarrollar un sistema simple de **cuenta bancaria** utilizando **Programación Orientada a Objetos (POO)** en Python.

El programa permite crear una cuenta bancaria y realizar operaciones básicas como:

- Consultar el saldo
- Depositar dinero
- Retirar dinero

El objetivo es aplicar conceptos fundamentales de la **POO**, como clases, atributos y métodos.

---

# 🎯 Objetivo del ejercicio

Desarrollar un programa que simule una **cuenta bancaria** que permita:

- Crear una cuenta con un titular y saldo inicial
- Consultar el saldo disponible
- Depositar dinero en la cuenta
- Retirar dinero de la cuenta

---

# 🧱 Estructura del proyecto
# ESTA ES LA CLASE
class CuentaBancaria:

    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    # DEPOSITAR DINERO
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    # RETIRAR
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print("Error: saldo insuficiente")

    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo}"


# MOSTRAR INFORMACION
cuenta1 = CuentaBancaria("Juan Perez", "001234567", 1000.0)
print(cuenta1.mostrarInformacion())
cuenta1.depositar(500.0)
cuenta1.retirar(2000.0)  # Muestra error si no alcanza
print(cuenta1.mostrarInformacion())
