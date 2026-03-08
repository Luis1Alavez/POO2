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