# calcular a lotação

#Dependendo da quantidade de vagas no hubi, o app irá exibira lotação
#sistema de cores: verde=vazio; amarelo=meio cheio; vermelho=cheio, 
#Dependendo da quantidade de vagas, será exibido uma mensagem explicando a situação
#foi considerado que existe apenas 1 hub no local

TOTAL_VAGAS='''quantidade total de vagas disponivel no HUB'''

#armazenando nessa lista a quantidade de vagas do Hubi
#pra calcular sua lotação 

hubs='''quantidade de vagas ocupadas no hubi'''
total_vagas=1 #para fins de exemplo
while hubs<=total_vagas: 
	if '''carro estaciona em uma vaga em determinada vaga''':
		hubs+=1
	if '''motorista sai da vaga''':
		hubs-=1

# exibir essa lotação

#Será apresentado um hub com lotação baixa com a cor verde, 
#Amarelo para lotação mediana e vermeho para um hub lotado
#Menor que 30% -verde
#Entre 30% e 60% -amarelo
#Entre 60% e 90% - laranja
#Entre 90% e 100% - vermelho

while True:
    porcentagem_hub = (hubs/TOTAL_VAGAS)*100
    if porcentagem_hub <= 30:
        '''cobrir o icone do hub com a cor verde'''
    elif porcentagem_hub <= 60:
        '''cobrir o icone do hub com a cor amarela'''
    elif porcentagem_hub <= 90:
        '''cobrir o icone do hub com a cor laranja'''
    elif porcentagem_hub <= 100:
        ''' cobrir o icone do hub com a cor vermelha'''
    if porcentagem_hub==100:
        print("Este Hubi está cheio")