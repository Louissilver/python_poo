class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo R${self.__saldo} do titular {self.__nome}")

    def depositar(self, valor):
        self.__saldo += valor

    def podeSacar(self, valorDeSaque):
        valorDisponivelParaSaque = self.__saldo + self.__limite
        return valorDeSaque <= valorDisponivelParaSaque

    def sacar(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
            print("Saque efetuado com sucesso!")
        else:
            print(f"O valor R${valor} passou do limite.")

    def transferir(self, valor, destino):
        if (self.__podeSacar(valor)):
            self.sacar(valor)
            destino.depositar(valor)
            print("Transferência efetuada com sucesso!")
        else:
            print(f"O valor R${valor} passou do limite.")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigoBanco():
        return "001"

    @staticmethod
    def codigosBancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
