#Básico
for i in range(101):
    print(i)

#Múltiplos de 2  entre 2 y 500
for i in range(2, 501, 2):
    print(i)

#Contando Vanilla ice
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")

#Wow. Número gigante a la vista
suma = 0
for i in range(0, 500001, 2):
    suma += i
print(suma)

#Regrésame al 3
for i in range(2024, 0, -3):
    print(i)

#Contador Dinámico
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)