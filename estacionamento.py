#Cronometrar o tempo de espera do motorista no HUB para mediante cobrança de estacionamento
import os
os.system("cls")
# data = dia que entrou (dd/mm/aa)
# d_saida = dia que saiu (dd/mm/aa)
# h_ent = hora que entrou (hora do dia)
# m_ent = minuto que entrou (minuto do dia)
# h_saida = hora que saiu
# m_saida = minuto que saiu
# lê placa e vincula a placa àquele cartão de estacionamento
data,h_ent,m_ent=0,0,0
d_saida,h_saida,m_saida=0,0,0
input (data,h_ent,m_ent).split() #será definido no momento que o motorista entra no estacionamento
h_ent=h_ent*60 #hora em minutos para facilitar contas
#recebe dados da Uber verificando se o veículo está cadastrado e com aplicativo funcionando
if '''veículo cadastrado''' and '''aplicativo ativo''':
    #aumentar carência de estacionamento de 20 para 30 minutos, definido pela equipe

input (d_saida,h_saida,m_saida)()
if d_saida-data==1:
	if (h_ent==23 and h_saida==0) and (m_saida+(60-m_ent))<=30:
		#liberar veículo sem pagamento de estacionamento
elif d_saida==data:
	if ((h_saida+m_saida)-(h_ent+h_ent))<=30:
		#liberar veículo sem pagamento de estacionamento
else:
		#verificar se cartão foi pago para liberar ou não a saída do veículo