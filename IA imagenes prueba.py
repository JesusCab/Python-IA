import csv
import math
import random
from functools import partial
rand = partial(random.randint)

def sigmoide(x):
    return 1/(1+math.exp(-x))

def producto_punto(v,w):
    return sum(x*y for x,y in zip(v,w))

def salida_neurona(pesos, entradas):
    return sigmoide(producto_punto(pesos, entradas))

def ffnn(red_neuronal, entrada):
    salidas = []
    for capa in red_neuronal:
        entrada = entrada + [1]
        #print("capa: ",capa, " \nentrada: ", entrada)
        salida = [salida_neurona(neurona,entrada) for neurona in capa]
        #print("salida: ", salida, "\n")
        salidas.append(salida)
        entrada = salida
    return salidas

def backpropagation(xor_nn, v_entrada, v_objetivo):
    salidas_ocultas, salidas = ffnn(xor_nn, v_entrada)
    salida_nuevo = []
    oculta_nuevo=[]
    alfa = 0.1 
    error = 0.5*sum((salida-objetivo)*(salida-objetivo) for salida, objetivo in zip(salidas, v_objetivo))
    salida_deltas = [salida * (1 - salida) * (salida - objetivo) for salida, objetivo in zip(salidas, v_objetivo)]
    for i, neurona_salida in enumerate(xor_nn[-1]):
        for j, salida_oculta in enumerate(salidas_ocultas + [1]):
            neurona_salida[j] -= salida_deltas[i] * salida_oculta*alfa
        salida_nuevo.append(neurona_salida)
        #print("pesos neurona salida: ", i, neurona_salida)
    ocultas_deltas = [salida_oculta * (1 - salida_oculta)* producto_punto(salida_deltas, [n[i] for n in xor_nn[-1]]) for i, salida_oculta in enumerate(salidas_ocultas)]
    for i, neurona_oculta in enumerate(xor_nn[0]):
        for j, input in enumerate(v_entrada + [1]):
            neurona_oculta[j] -= ocultas_deltas[i] * input * alfa
        oculta_nuevo.append(neurona_oculta)
        #print("pesos neurona oculta: ", i, neurona_oculta)
    return oculta_nuevo, salida_nuevo, error

def random_nn():
    random.seed(7)
    xor_nn =[
        [
            [
                rand(-100,100)/100, rand(-100,100)/100, rand(-100,100)/100
            ],
            [
                rand(-100,100)/100, rand(-100,100)/100, rand(-100,100)/100
            ]
        ],
        [
            [
                rand(-100,100)/100, rand(-100,100)/100, rand(-100,100)/100
            ]
        ]
    ] 
    return xor_nn

tamaño_entrada = 784
numero_ocultas = 15
tamaño_salida = 10
nn = []
i= 0

def pesos():
    random.seed(7)

    capa_oculta = [ [random.randint(-100,100)/100 for _ in range(tamaño_entrada + 1)] for  _ in range(numero_ocultas)]
    capa_salida = [ [random.randint(-100,100)/100 for _ in range(numero_ocultas + 1)] for  _ in range(tamaño_salida)]

    return capa_oculta, capa_salida

def readcsv(archivo):
    input = open(archivo, "r")
    reader = csv.reader(input, delimiter=",")
    rownum = 0
    a = []
    for row in reader:
        a.append(row)
        rownum += 1 
    input.close()
    return a

datos = readcsv(r'\Users\jesus\Desktop\Inteligencia Artificial\mnist_train.csv')

objetivos=[[1 if i==j else 0 for i in range(10)] for j in range(10)]

capa_oculta, capa_salida = pesos()
nn = [capa_oculta, capa_salida]

i = 0
for input in datos[1:]:
    oculta, salida, error = backpropagation(nn, [int(x)/255*2-1 for x in input[1:]], objetivos[int(input[0])])
    if i%100==0:
        print (i, error)
    nn= [oculta, salida]
    i=i+1

test = readcsv(r'\Users\jesus\Desktop\Inteligencia Artificial\mnist_test.csv')
ffnn(nn, [int(x)/255*2-1 for x in test[1][1:]])[-1]

suma = 0

for input in test[1:]:
    salida = ffnn(nn, [int(x)/255*2-1 for x in input[1:]])[-1]
    digito = [i for i, j in enumerate(salida) if j==max(salida)]
    if digito[0] ==int(input[0]):
        suma=suma+1

print(suma/len(test)*100)
