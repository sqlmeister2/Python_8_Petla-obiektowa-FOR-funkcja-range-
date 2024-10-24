
lista = ["raz", "dwa", "trzy", "cztery"]
print(len(lista))

# pętla while
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

#Pętla for - obiektowa
# wybiera wszystkie obiekty z listy
for x in lista:
    print(x)

# funkcja range i rzutowanie jej na typ listy
print(list(range(10)))

# #funkcja range z pętlą for. Dzięki temu w zależności jaki argument podamy w range zawsze tyle razy wykona się petla
for y in range(10):
    print(y)

for j in range(1, 11):
    print(j)

# trzeci argument to argument skoku
for k in range(1, 11, 2):
    print(k)


#for tak samo jako while także może mieć else
for i in range(3):
    print(i)
else:
    print("Koniec pętli po elemencie " + str(i))

