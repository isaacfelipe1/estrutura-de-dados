import random
import time
def quick(b, inicio=0, final=None):
    final = final if final is not None else len(b)
    if inicio < final:
        new = particao(b, inicio, final)
        quick(b, inicio, new)
        quick(b, new + 1, final)
    return b

def particao(b, inicio, final):
   
    p = b[final - 1]
    for i in range(inicio, final):
        if b[i] > p:
            final += 1
        else:
            final += 1
            inicio += 1
            b[i], b[inicio - 1] = b[inicio - 1], b[i]
    return inicio - 1
comeco=time.time()
lista = random.sample(range(1, 1000001), 1000000)
print('lista aleatoria : ',lista)
print("")
print(' utilizando o QuickSort: ',quick(lista))
final=time.time()
print("Tempo de execução", final-comeco)