#Importamos os dados da Uber e salvamos cada veículo em um dicionário, com a mesma key para identificá-los
#segue exemplo
d_veiculo={0:'Ford KA',1:'Ford Fiesta',2:'Classic',3:'Onix',4:'Ford KA',5:'Sandero'}
d_motorista={0:'Ferdinando Pereira',1:'Luciana Barreto',2:'Aldo Silva',3:'Anderson Souza',4:'Gabriel Lima',5:'Luana Gomes'}
d_placa={0:'ADS-1234',1:'DFG-4566',2:'GFH-4578',3:'OYT-7654',4:'BGT-6754',5:'JBL-9876'}

#verificando se a vaga está livre:
'''Através de um sensor da vaga ele vai mandar um valor 
maior que zero para o telão caso ela esteja ocupada
Se ela não tiver ocupada o valor será 0 e mostrará 
que a vaga está livre'''

vaga = int(input("Vagas livres"))
if vaga == 0:
    print("A vaga está livre")
else:
    print("A vaga está ocupada")

#colocando a vaga no telão:

#Câmera lendo a placa do carro:
placa = input("Ler placa")
#Fizemos uma lista para simular onde as placas ficarão guardadas depois de lidas
telao = []
#preenchendo a lista com a placa do carro lida pela câmera
telao.append(placa)
#mostrando a placa no telao 
print(placa[len(placa)-1])

##Mostrar veiculos disponiveis no telão :
veiculos = {1:'KGB54', 2: 'LPU880', 3: 'ASD54', 4: 'ASD45'}
valor = int(input())
resultado = veiculos[valor]
if valor == 1:
  print("O veículo de placa:", resultado, "Está disponível")
elif valor == 2:
  print("O veículo de placa:", resultado, "Está disponível")
elif valor == 3:
  print("O veículo de placa:", resultado, "Está disponível")
elif valor == 4:
  print("O veículo de placa:", resultado, "Está disponível")
else:
  print("NÃO TEM NENHUM MOTORISTA LIVRE ")

#o nome dos motoristas será mostrado no telão com o sobrenome censurado:

nome = 'Felipe Silva'
sobrenome=nome.split()
nome = sobrenome[(len(sobrenome))-1]
letras_sobrenome=list(nome)
sobrenome_LGPD=""
for a in range (len(nome)):
    if a!=0 and a!=(len(nome)-1):
        var='*'
    else:
        var=str(nome[a])
    sobrenome_LGPD=sobrenome_LGPD+ var
print(sobrenome_LGPD)

