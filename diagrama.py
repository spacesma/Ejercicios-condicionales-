print("Quiero cocinar arroz")
arroz_hecho = input("Tengo arroz hecho?")
if arroz_hecho == "si":
    print("Como arroz")
else:
    print("Hago arroz")
    tipo_arroz = input("¿Graneado o blanco?")
    if tipo_arroz == "Graneado":
        print("Hervir")
    else:
        print("Lavar arroz")
    print("comer")