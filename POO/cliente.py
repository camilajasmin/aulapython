# declaração da classe Cliente
# esta classe permite que sejam criados novos objetos 
# do tipo cliente
class Cliente:
    # a implementação do método __init__representa a 
    # contrução do método construtor da classe, responsável
    # por inicializar o objeto que será criado.
    # este método possui o argumento self que faz referência à própria classe.
    # quando for criar um método de classe deve-se utilizar do comando
    # self para referenciar a própria estrutura de classe a qual ele pertence.
    # note que no método __init__(construtor) foram iniciados os atributos de 
    # da classe, representando as características do cliente
    # todos eles foram criados utilizando o comando self, que indica que eles 
    # pertencem a classe Cliente. 
    # os atributos foram declarados como privados (2 undescores)
    ''' A classe Cliente gera novos clientes e pede alguns dados pessoais, além de ser capaz de realizar a gravação deste cliente'''
    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__genero = ""
        self.__mail = ""
    # o métodos dados é utilizados para realizar a passagem dos dados do cliente para a classe Cliente
    
    def dados(self, nome = "", idade = 0, genero = "", mail = ""):
        ''' O método dados pede algumas informações do cliente para que ele seja salvo no sistema '''
        self.__nome = nome 
        self.__idade = idade
        self.__genero = genero
        self.__mail = mail
    # o método gravar exibe uma mensagem com o nome do cliente dizendo que foi salvo com sucesso
    def gravar(self):
        ''' O método gravar exibe uma mensagem com o nome do cliente e gravação realizada com sucesso'''
        print("O cliente " +self.__nome+ " foi gravado com sucesso")