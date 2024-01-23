from classCB import ContaBancaria
class ContaCorrente(ContaBancaria):

    def __init__(self):
        self.__limite = 0.0
    
    def abrirConta(self, NB = 0, NA = 0, NC = "", titular = "", saldo = 0.0, limite = 0.0):
        self._nBanco = NB
        self._nAgencia = NA
        self._nConta = NC
        self._titular = titular
        self._saldo = saldo
        self.__limite = limite
        print("A conta " +str(self._nBanco)+ " do sr(a)."+self._titular+" foi aberta com sucesso!")

    def sacar(self, valor):
        if (valor > self._saldo + self.__limite):
            print("Saldo insuficiente!")
        elif (valor <= self._saldo):
            self._saldo -= valor
            print("Você ralizou um saque de R$"+str(valor)+". Portanto, o seu saldo atual é de R$" +str(self._saldo))
        else:
            sobra = valor - self._saldo
            self.__limite -= sobra
            self._saldo = 0 
            
            print("O valor sacado é de R$" +str(valor)+ ". \n O saldo atual é de R$" +str(self._saldo)+". \n E o seu limite atual é de R$"+str(self.__limite))