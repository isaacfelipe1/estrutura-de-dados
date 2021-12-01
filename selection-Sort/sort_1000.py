import sys
import random
import time
def inicio():
    inicio=time.time()
    vetor = random.sample(range(1, 1001), 1000)
    print('lista aleatoria: ',vetor)
    sort(vetor)
    print('Selection Sort: ', vetor)
    final=time.time()
    print("Tempo de execução", final-inicio)
def sort(vetor):
    for i in range(len(vetor)):
        index = i
        for t in range(i+1, len(vetor)):
            if vetor[index] > vetor[t]:
                index = t
        vetor[i], vetor[index] = vetor[index], vetor[i]

if __name__ == '__main__':
    inicio()


