num = int(input("digite o número desejado para saber se ele pertence à sequência Fibonacci"))

a = 0
b = 1
contador=0
cont=0
while contador < num:
    c = a + b
    a = b
    b = c
    contador +=1
    if c == num:
        print(" o numero ",num," pertence à sequência")
        cont+=1
if cont == 0 :
    print(" o numero ",num," não pertence à sequência")
    