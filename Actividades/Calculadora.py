#Calculadora de propina

total = float(input("Cuenta: ")) # pido el total de la cuenta
propina = float(input("Propina %: ")) # pido el porcentaje de propina
propina_total = total * propina / 100 # calculo la propina
print("Propina:", propina_total) # muestro la propina calculada
print("Total a pagar:", total + propina_total) # muestro el total a pagar incluyendo la propina