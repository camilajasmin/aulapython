import os
class Cliente:
    def __init__(self):
        self.__nome = ""
        self.__email = ""
        self.__cpf = ""
        self.__idade = 0
        self.__telefone = ""

    def gravarCliente(self, nome="", email="", cpf="", idade=0, telefone=""):
        if (nome=="" 
            or email=="" 
            or cpf=="" 
            or idade < 18 
            or telefone == "" 
            or not cpf.isnumeric() 
            or len(cpf) != 11
            or len(telefone) != 9
            or email.find("@") ):
            print("DIGITE TODOS OS CAMPOS CORRETAMENTE!")
        else:
            
            self.__nome = nome
            self.__email = email
            self.__cpf = cpf
            self.__idade = idade
            self.__telefone = telefone
            self.__gravar()
    def __gravar(self):

        arquivo = open("dados/infocliente.csv", "a")
        arquivo.write("nome: " +self.__nome+";\n")
        arquivo.write("email: " +self.__email+";\n")
        arquivo.write("cpf: " +self.__cpf+ ";\n")
        arquivo.write("idade: " +str(self.__idade)+ ";\n")
        arquivo.write("telefone: " +self.__telefone+ ";\n")
        arquivo.write("-----------------------------------\n")
        arquivo.close()
        print("Cliente gravado com sucesso")