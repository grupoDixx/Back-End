import os, threading, queue
import threading
import queue
os.system("cls")

#selecionar o HUBi no aplicativo
destino='xxxx' #xxxx é um endereço inexistente
destino=(input('Digite o endereço:'))
#pode adicionar até 2 paradas
if destino != 'xxxx':
	if '''apertar botão para adicionar parada''':
		destino1=(input('Digite o endereço:'))
		if '''tocar na tela para mudar a ordem das paradas''':
			if '''apertar botão para adicionar parada''':
				destino2=(input('Digite o endereço:'))
				if '''tocar na tela para mudar a ordem das paradas''':
#receber 'toque na tela' para pedir o veículo
#enviar dados aos veículos aptos a receber a corrida
#mostrar tela de espera enquanto alguém não aceita o veículo

	if '''veículo aceitou a corrida''':
		#receber dados de onde o veículo está e criar vetor com seguintes dados:
		car=['''modelo do veículo''','''nome do motorista''',
				'''foto do motorista''','''nota''',
				'''vaga em que está estacionado''']
		print(f'Veículo: {car[0]}\n{car[1]}\n{car[2]}\n{car[3]}\nEstá na vaga {car[4]}')
	else:
		print('''mostrar na tela o mapa com a distância do veículo do local''')
	#exibir opção de cancelar a corrida
	if '''apertar um botão para cancelar a corrida''':
		#enviar relatório do cancelamento à empresa de motorista de aplicativo
		if ('''hora atual'''-'''hora que o veículo aceitou a corrida''')==
				('''intervalo de tempo determinado pelo aplicativo'''):
			#cobrar valor a título de multa de cancelamento
		else:
			#voltar à tela inicial do aplicativo

#é necessario saber o numero de vagas disponíveis no HUB

quantidade_motoristas=6 #número exemplificativo

if quantidade_motoristas==1:
    print(f"Sim, existe {quantidade_motoristas} veículo disponível no HUB. ")
elif quantidade_motoristas>=1:
    print(f"Sim, existem {quantidade_motoristas} veículos disponíveis no HUB. ")
else:
    print("Nao existem veículos disponíveis no HUB")
##verificando se existem motoristas no Hubi
#Utilizando fila virtual dos motoristas (filaMotoristas)
filaMotoristas=7 #exemplo

print("Há ",len(filaMotoristas)," motoristas disponíveis.")

filaPassageiros = queue.Queue(maxsize=0)
if '''Há motorista disponível''':
    while True:
        for i in range(filaPassageiros):
            if  '''passageiro entrou na fila de espera''':
                filaPassageiros.put(i+1)
                print(filaPassageiros)
                print("Você está na posição ",i+1, "na lista")
            elif '''motorista pegou seu passageiro ou chegou ao HUB''':
                filaPassageiros.get(i+1)
                print(filaPassageiros)
else:
    print("No  momento não há motoristas disponíveis!")
    espera=str(input("Deseja esperar na fila[S/N]?"))
    espera = espera.upper()
    if espera=="S":
        '''Esperar a lista de motorista atualizar e ficar algum disponível.'''
    else:
        break

#funcionalidade da fila de passageiros no aplicativo

#Usando uma lista seguindo a regra FIFO (primeiro a entrar e também primeiro a sair)
#Maxsize corresponde ao tamanho limite da lista, 
#o qual é zero e, portanto, é uma fila infinita. (num de vagas)

#queue.Queue é a sintaxe de uma fila

filaPassageiros = queue.Queue(maxsize=0) #número limite de vagas
for i in range (len(filaPassageiros)):
    if  '''passageiro entrou na fila de espera''':
        filaPassageiros.put(i+1)
		#"posicao_na_fila" é a variável que mostra a posição
		#variável que identifica o passageiro na fila = "passageiro"
		if '''passageiro''' in filaPassageiros:
			print(f"você é o {'''posicao_na_fila'''} da fila")
		elif ('''passageiro aleatório pegou seu uber''' or '''passageiro aleatório desistiu da fila''') and '''posição da pessoa que desistiu<posição do passageiro''':
		    # recebe dados que alguém saiu da fila no sistema da pessoa que saiu/desistiu: filaPassageiros.get(i+1)
			print(f"você é o {'''verificar posição na fila'''} da fila")
			if '''passageiro ser o próximo da fila''':
				print("Você é o próximo da fila")
	if '''passageiro decidir sair da fila antes de sua vez''':
		input('''recebe comando para sair da fila''')
		filaPassageiros.get(i+1)
		break
    elif '''veículo do passageiro chegou''':
		print(f"Se dirija ao veículo {'''dados do veículo'''}")	