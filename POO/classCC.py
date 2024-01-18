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