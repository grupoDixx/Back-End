#fizemos um arquivo txt com uma simulação de banco de ddados
arquivo = open("arquivo.txt", "r", encoding="utf8")
print(arquivo.read())
arquivo.close()