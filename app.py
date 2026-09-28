# Programa de pesquisa de satisfação
# Autor: Maria Clara Lima

# Entrada
nomes = []
idades = []
respostas = []

# Processamento
for i in range(50):
    nome= input("Digite seu nome: ")
    nomes.append(nome)
    idade= int(input("Digite sua idade: "))
    idades.append(idade)
    resposta= input("Digite Excelente, Bom ou Ruim de acordo com sua satisfação: ")
    respostas.append(resposta)

# Saída
print(respostas.count("Excelente"), "excelentes")
print(respostas.count("Ruim"), "ruins")