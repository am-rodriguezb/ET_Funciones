from funcion2 import *

lista=[["amaro", 20, "lol"],
    ["alex", 14, "war"] 
]

menu=True
while menu:
    print("1 guardar dato")
    print("2 buscar dato")
    print("3 salir")
    op=int(input("Elije opcion"))
    if op ==1:
        print()
        guardar_dato(lista)
    elif op ==2:
        print()
    elif op ==3:
        menu=False
    else:
        print("no valido")