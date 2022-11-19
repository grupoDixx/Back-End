import os, threading, queue
import threading
os.system("cls")
#para mostrar quantos carros estão esperando, é necessário saber a 
# quantidade de vagas no hub
quantidade_motoristas=6 
hub =8
if quantidade_motoristas>=1:
    if quantidade_motoristas<=hub:
        print("Existem ", quantidade_motoristas, "motoristas no HUB")
    else:
        motoristas_hub=quantidade_motoristas-hub
        print("O hub esta cheio, e existem ", (motoristas_hub), " motoristas na fila de espera")
else:
    print("Nao existem motoristas esperando no hub")

'''
usar geolocalização por API, para utilizar a localização do celular, 
pegando latitude e longitude. Considere "lat_driver" e "lon_driver"
disponível em https://pypi.org/project/haversine/
'''
#pip install haversine
from haversine import haversine, Unit
#para fins de exemplo:
lat_driver,lon_driver=48.8567, 2.3508 #referente à cidade de Paris, na França
lat_hubi,lon_hubi=45.7597, 4.8422 # referente à cidade de Lyon, na França
driver=(lat_driver,lon_driver)
hubi=(lat_hubi,lon_hubi)
haversine (hubi,driver) #distância em quilômetros entre o hubi e o motorista

#fazendo fila virtual de motoristas

#Usando uma lista seguindo a regra FIFO(primeiro a entrar e também primeiro a sair)

#Maxsize corresponde ao tamanho limite da lista, o qual é zero e,
#portanto, é uma fila infinita. (num de vagas)

#queue.Queue é a sintaxe de uma fila

filaMotoristas = queue.Queue(maxsize=0)#número limite de vagas
for i in range (len(filaMotoristas)):
    if  '''motorista entrou na fila de espera''':
        filaMotoristas.put(i+1)
        print(filaMotoristas)
    elif '''motorista pegou seu passageiro ou chegou ao HUB''':
        filaMotoristas.get(i+1)
        print(filaMotoristas)

print("No  momento o HUB está lotado! Tente mais tarde.")

#opção de o motorista confirmar ou cancelar

if '''motorista dentro do raio de distância do HUBi''':
    while True:
        #celular do motorista recebe dados do passageiro:
        corrida='a'
        passageiro=['nome', 'nota','destino']
        print(f'{passageiro[0]}\n{passageiro[1]}\n{destino[2]}')
        corrida=input('Aceitar corrida? S/N').upper()
		#coloquei S/N, mas deve ser feito por meio do toque na tela
        if corrida=='N':
            break
			#break, com comando para retornar à tela inicial
        if corrida=='S':
			#ligar o gps direcionando o motorista para o HUBi
			#se houver fila de motoristas, coloca o motorista na fila
            if '''motorista resolver cancelar corrida''':
                #apertar um botão para cancelar a corrida
                #enviar relatório do cancelamento à empresa de motorista de aplicativo
                #Se cancelamento ocorrer após entrada em eventual fila de espera,
                # o motorista é retirado da fila
                #break, e voltar à tela inicial do aplicativo
                break

if corrida=='S':
    #mapa do aplicativo mostrará o caminho ao HUB.i para o motorista
    #exemplo:
    mapa=input("vamos lá?")
    mapa=mapa.lower()
    if mapa=="s" or mapa=="sim":
        if '''passageiro precisar virar a esquerda''':
            print("vire à esquerda")
        elif '''passageiro precisar virar a direita''':
            print("vire à direita")
        else:
            print("siga em frente")

    if '''passageiro chegar ao HUB.i''':
        print("você chegou ao seu destino")

#indicar para qual vaga o motorista deve se dirigir
#é necessario saber a quantidade de vagas que existem no HUB
'''apos o motorista aceitar a corrida e confirmar a ida ao 
HUB ira aparecer uma tela designando para qual vaga ele ira seguir'''
#escolher vaga livre aleatoriamente.
#cada número é referente a uma vaga específica
vagas = {1:'vaga 1', 2: 'vaga 2', 3: 'vaga 3', 4: 'vaga 4'}
vaga=[0,0,0,0] #recebe dos sensores. Vaga ocupada = 1, vaga livre = 0
checagem = [0,0,0,0] #para conferir se a vaga realmente está ocupada
for i in range (len(vaga)):
    if checagem[i]==0:
        print(f"Voce deve se dirigir a: {vagas.get(i+1)}")
        checagem [i]=1
        if ('''intervalo de tempo'''>'''2 minutos''') and vaga[i]==0:
            checagem[i]=0
        break

