class User:
    def __init__(self):
        self.__nomeuser = ""
        self.__senha = ""
        self.__mail = ""
        self.__nvlacesso = ""
    def setData(self, nomeuser, senha, mail, nvlacesso):
        self.__nomeuser = nomeuser
        self.__senha = senha
        self.__mail = mail
        self.__nvlacesso = nvlacesso
    def authenticated(self):
        print()