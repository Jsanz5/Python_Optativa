#Jolman & Joel


resultado1 = 15 % 4 #Operador módulo
print(resultado1)

resultado2 = 3 ** 4 #Operador potencia
print(resultado2)

resultado3 = 10 // 3 #Operador división
print(resultado3)

if(resultado1 > 0 and resultado2 > 0): #validamos que las dos condiciones sean verdaderas
    print("Ambos resultados son positivos")

if(resultado1 > 0 or resultado2 > 0): #validamos que al menos una de las condiciones sea verdadera
    print("Al menos uno de los resultados es positivo")

if (not(resultado1 > 0)): #validamos que ninguna de las condiciones sea verdadera
    print("Ninguno de los resultados es positivo")
else:
    print("Al menos uno de los resultados es positivo")
       