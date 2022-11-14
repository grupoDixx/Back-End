
#Camera lendo a placa do carro
placa = input("Ler placa")
#Fizemos uma lista para guardar as placas depois de lidas
telao = []
#preenchendo a lista com a placa do carro lida pela camera
telao.append(placa)
#mostrando a placa no telao 
print(placa)
#Através de um sensor da vaga ele vai mandar um valor maior que zero para o telão caso ela esteja ocupada
#Se ela não tiver ocupada o valor será 0 e mostrará que a vaga está livre 
vagas = {1:'vaga 1', 2: 'vaga 2', 3: 'vaga 3', 4: 'vaga 4'}
cod = int(input())
disponiveis = vagas[cod]
if cod == 1:
    print("A vaga 1 está livre")
elif cod == 2:
    print("A vaga 2 está livre")
elif cod == 3:
    print("A vaga 3 está livre")
elif cod == 4:
    print("A vaga 4 está livre")
else:
    print("A vaga está ocupada")
##Mostrar veiculos disponiveis no telão 
veiculos = {1:'KGB54', 2: 'LPU88', 3: 'ASD54', 4: 'ASD45'}
valor = int(input())
resultado = veiculos[valor]
if valor == 1:
   print("O veículo de placa:", resultado, "Esta disponível")
elif valor == 2:
  print("O veículo de placa:", resultado, "Está disponível")
elif valor == 3:
  print("O veículo de placa:", resultado, "Está disponível")
elif valor == 4:
  print("O veículo de placa:", resultado, "Está disponível")
else:
  print("NÃO TEM NENHUM MOTORISTA LIVRE ")