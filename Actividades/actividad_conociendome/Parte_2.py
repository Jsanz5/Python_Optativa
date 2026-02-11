#Parte 2 – Gustos personales

#Pide al usuario tres cosas que le gusten (por ejemplo: leer, música,viajar).
gusto_1 = input("Dime 1 gusto que tengas: ")
gusto_2 = input("Dime otro gusto que tengas: ")
gusto_3 = input("Dime un ultimo gusto que tengas: ")
gustos=[gusto_1,gusto_2,gusto_3]
print("Tus gustos son,", gustos, ".")
print("Tienes" , len(gustos) , "gustos en tu lista.")

gustos_modificados=gustos * 2
print("Lista de gustos modificadas 2 veces", gustos_modificados)