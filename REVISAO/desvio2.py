# este programa exibe uma mensagem para os motoristas que estão com o seu veículo em dia de rodízio
finalPlaca = input("Digite o último número da placa do seu carro: ")

if (finalPlaca == "1" or finalPlaca == "2"):
    print("Seu carro está no dia de rodízio! - Segunda Feira")
elif(finalPlaca == "3" or finalPlaca == "4"):
    print("Seu carro está no dia de rodizio! - Terça Feira")
elif(finalPlaca == "5" or finalPlaca == "6"):
    print("Seu carro está no dia de rodizio! - Quarta Feira")
elif(finalPlaca == "7" or finalPlaca == "8"):
    print("Seu carro está no dia de rodizio! - Quinta Feira")
elif(finalPlaca == "9" or finalPlaca == "0"):
    print("Seu carro está no dia de rodizio! - Sexta Feira")
else:
    print("Final de placa incorreto ")



