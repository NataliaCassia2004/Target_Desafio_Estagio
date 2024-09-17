import re
lista_faturamento = ["SP – r$67836.43","RJ – r$36678.66","MG – r$29229.88","ES – r$27165.48","OUTROS – r$19849.53"]
lista_valores=[]
lista_estados=[]
lista_porcentagem=[]


#para transformar a lista faturamento em uma lista apenas com numeros para realizar os calculos
for i in lista_faturamento:
    aux_estados = (re.sub('[^A-Z]', '', i))
    lista_estados.append(aux_estados)

    aux =  float(re.sub('[^0-9.]', '', i))
    lista_valores.append(aux)
    
#100%
soma = sum(lista_valores)

#porcentagem estados
for i in lista_valores:
    representacao = (i*100)/soma
    lista_porcentagem.append(representacao)

#printando
for i in range(0,len(lista_estados)):
    print("O estado de ",lista_estados[i], f" teve {lista_porcentagem[i]:,.2f}% de representação dentro do valor total mensal da distribuidora.")


