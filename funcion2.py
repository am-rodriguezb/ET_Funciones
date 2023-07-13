def guardar_dato(lista):
    nombre=input()
    edad=int(input())
    juego=input()
    lista_a=[nombre, edad, juego]
    lista.append(lista_a)
    return lista
