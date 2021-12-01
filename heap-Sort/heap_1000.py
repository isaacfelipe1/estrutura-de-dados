import time #Importando a hora para exercursão
import random #importando o random para números aleatorios
def heapify(lista, tamanho_da_pilha, i):
    maior_valor = i # Inicializar o maior como raiz
    esquerda = 2 * i + 1  # esquerda = 2*i + 1
    direita = 2 * i + 2  # direita = 2*i + 2
    #Testando a númeração da esquerda
    if esquerda < tamanho_da_pilha and lista[i] < lista[esquerda]:
        maior_valor = esquerda
    #Testando a númeração da direita
    if direita< tamanho_da_pilha and lista[maior_valor] < lista[direita]:
        maior_valor = direita
    #para troca de valores
    if maior_valor != i:
        lista[i], lista[maior_valor] = lista[maior_valor], lista[i] 
        heapify(lista, tamanho_da_pilha, maior_valor)
# A função de ordenação
def heapSort(lista):
    tamanho_da_pilha = len(lista)
    #Construindo um maxheap.
    for i in range(tamanho_da_pilha // 2 - 1, -1, -1):
        heapify(lista,tamanho_da_pilha, i)
    # para extrair os valores
    for i in range(tamanho_da_pilha - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

#main
comeco=time.time()
lista = random.sample(range(1, 1001), 1000)
numero_da_pilha= len(lista)
for i in range(numero_da_pilha):
    print("%i" % lista[i]),
heapSort(lista)
numero_da_pilha= len(lista)
print()
print('Númeração organizada:' )
for i in range(numero_da_pilha):
    print("%i" % lista[i]),
fim_exercusao=time.time()
print("Tempo de execução :", fim_exercusao-comeco)