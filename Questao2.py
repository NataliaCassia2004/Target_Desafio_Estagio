#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


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
    
