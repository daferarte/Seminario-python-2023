numero=0
print("Tabla del 7")
# ciclo wuile para la tabla del 7
while numero<=10:
    # print("7X"+str(numero)+"="+str(numero*7)) # manera nativa de concatenar variables
    print(f'7 X {numero} = {numero*7}') #intrapolacion de texto y variables
    numero += 1
print("fin")