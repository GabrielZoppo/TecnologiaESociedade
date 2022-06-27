# Importação das bibliotecas
import random

# Declaração das variáveis
T = -1 # Lista Tabu
Iter = 0 # Atual Iteração --> Critério de Parada
MelhorIter = 0; # Iteração da melhor solução -- Solução com o maior Fitness
BTMax = 2 # Critério - Nº de iterações sem melhora no meu fitness / solução
p = [] # Lista com os pesos dos itens
b = [] # Lista com os beneficios dos itens
PesoMax = 23 # Capacidade da mochila
numItens = 5 # Nº de itens disponiveis
alpha = 10 # Penalidade para quando passar o peso

# Função Fitness 
def Funcao_Avaliacao(solucao, peso, beneficio, PesoMax):
  soma_peso = 0  
  soma_beneficio = 0
  for i in range(0,(numItens)):
    soma_peso += peso[i]*solucao[i] 
    soma_beneficio += beneficio[i]*solucao[i]
  avaliacao = soma_beneficio - alpha *(max(0, (soma_peso - PesoMax)))
  return avaliacao

# Gera os vizinhos da solução
def GeraVisinhos(melhor_solucao,quantidade_vizinhos):
    vizinhos = []
    posicao = 0
    for i in range(0, quantidade_vizinhos):
        vizinho = []
        for j in range(0, len(melhor_solucao)):
            if  j == posicao:
                if melhor_solucao[j] == 0:
                    vizinho.append(1)
                else:
                    vizinho.append(0)
            else:
                vizinho.append(melhor_solucao[j])
        vizinhos.append(vizinho)
        posicao += 1
    return vizinhos

# Faz a uma lista de avaliação de todos os vizinhos
def AvaliaVizinhos(V,peso, beneficio,pesoMax):
		Fitness_Vizinhos = []
		for i in range(0,len(V)):
  			Fitness_Vizinhos.append(Funcao_Avaliacao(V[i],peso,beneficio,PesoMax))
		return Fitness_Vizinhos

# Obtem a posição do melhor vizinho e verifica se for fruto de um movimento TABU, se for retorna o segundo melhor
def obter_posicao_melhor_avaliacao(Fitness_Vizinhos,T,sbest, V):
    maxima_avaliacao = max(Fitness_Vizinhos)
    posicao = 0
    movimento_Tabu = T

    for i in range(0, len(Fitness_Vizinhos)):
        if Fitness_Vizinhos[i] == maxima_avaliacao:
            posicao = i
            break
    
    if movimento_Tabu != -1:
        posicao_objeto = encontra_Posicao_Vizinho(sbest, V[posicao])
        if posicao_objeto == movimento_Tabu:
            melhor_posicao = 0
            for i in range(1, len(Fitness_Vizinhos)):
                if i != posicao_objeto:
                    if Fitness_Vizinhos[i] > Fitness_Vizinhos[melhor_posicao]:
                        melhor_posicao = i
            return melhor_posicao 
    return posicao 


# Definir aleatóriamente o valor da primeira solução
s = []
for i in range(0,numItens):
  num = random.randint(0,1)
  s.append(num)
# Definir aleatóriamente os valores de peso e beneficio
for i in range(0,numItens):
  peso = random.randint(0,10)
  beneficio = random.randint(0,10)
  p.append(peso)
  b.append(beneficio)

sbest = s

# Faz a primeira iteração
Fitness = Funcao_Avaliacao(s,p,b,PesoMax)
Aspiracao = Fitness

# Entra no loop para fazer as demais iterações
while(Iter - MelhorIter < BTMax):
  	
    print("1º Iteração:", Iter)
    print("Fitness:",Aspiracao)

    Iter +=1
    V = GeraVisinhos(s,numItens)
    print("")
    print("{}ª Iteração:".format(Iter))
    print("Vizinhos:",V)
  	
    FitnessVizinhos = AvaliaVizinhos(V,p, b,PesoMax)
    posMelhorFitness = obter_posicao_melhor_avaliacao(FitnessVizinhos,T,s, V)
    if Aspiracao < FitnessVizinhos[posMelhorFitness]:
  		T = posMelhorFitness
  		s = V[posMelhorFitness]
  		sbest = s
  		Aspiracao = FitnessVizinhos[posMelhorFitness]
  		print('Melhor Vizinho:', s)
  		print('Fitness do melhor Vizinho:',Aspiracao)
  		print('Aspiração:',Aspiracao)		
  		print('Posição do melhor vizinho:',posMelhorFitness)
  		print("Lista Tabu:", T)
  		MelhorIter += 1
  	else:
  		F = FitnessVizinhos[posMelhorFitness]
  		print('Melhor Vizinho:', s)
  		print('Fitness do melhor Vizinho:',F)
  		print('Aspiração:',Aspiracao)
  		print('Posição do melhor vizinho:',posMelhorFitness)
  		print("Lista Tabu:", T)
  		s = V[posMelhorFitness]

Iteracoes = []
MelhorSolucao = []

print("")
print("Total de iterações:",Iter)
print("Melhor Solução:",sbest)
print("Melhor Fitness:",Aspiracao)  
