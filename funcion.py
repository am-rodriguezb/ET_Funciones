def puntacion(clase):
    return sum(clase) / len(clase)

clase=[1,2,3,4]
media=puntacion(clase)
print(media)

clase=[234,435,12]
print(puntacion(clase))