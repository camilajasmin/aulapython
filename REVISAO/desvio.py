# este programa obtem o nome do aluno e a nota média
# se o aluno obtiver uma média acima ou igual a seis o aluno será APROVADO
# caso contrário, ele será REPROVADO

nome = input("Digite o nome do aluno: ")
media = float(input("digite a nota média do aluno: "))

if (media >= 6):
    print("Aprovado")
else:
    print("Reprovado")