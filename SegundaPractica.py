edad = 21
altura = 1.88

edadString = str(edad)

print(edad + edad)
print(edadString + edadString)
print(type(edad))
tuEdad=input("Introduce tu edad: ")
tuEdad=int(tuEdad)

#Estructura if
if tuEdad >= 18:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("Eres inmortal jaja salu2")
elif tuEdad <= 0:
    print("No existes jaja salu2")
else:
    print("No eres mayor de edad")

#Estructura for
for i in range(0, 10):
    print(i)

