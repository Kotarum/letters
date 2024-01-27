import matplotlib.pyplot as plt
import numpy as np


def contar_letras(lista, conte):
    return len([letra for letra in conte if letra.lower() in lista])

# Divide el texto en fragmentos del mismo tamaño
def clasificar_letras(texto, tamaño):
    total_letras = len(texto)
    resultados = []
    
    n = 0
    while total_letras >= tamaño:
        grupo_letras = []
        #print(grupo_letras)
        for numletras in range(n*tamaño, n*tamaño + tamaño):
            grupo_letras.append(texto[numletras])
            #print(grupo_letras)
        #grupo_letras = contar_letras(grupo_letras)
        n = n + 1
        #print(n)
        total_letras = total_letras - tamaño
        #print(total_letras)
        unido = ''.join(grupo_letras)
        resultados.append(unido)
        #print(resultados)
    return resultados
    

def contar_letras_lista(letras_a_contar, lista):
    nvocales = []
    for x in range(len(lista)):
        nvocales.append(contar_letras(letras_a_contar, lista[x]))
    return nvocales



with open('el_quijote.txt', encoding="utf-8") as file:
    cosas = file.read()

#cosas.split
lista_palabras = clasificar_letras(cosas, 100)

avocal = contar_letras_lista(['a','á'], lista_palabras)
evocal = contar_letras_lista(['e','é'], lista_palabras)
ivocal = contar_letras_lista(['i','í'], lista_palabras)
ovocal = contar_letras_lista(['o','ó'], lista_palabras)
uvocal = contar_letras_lista(['u','ú'], lista_palabras)
vocales = [avocal, evocal, ivocal, ovocal, uvocal]



fig = plt.figure(figsize=(10,7))
#ax = fig.add_axes(['a', 'e', 'i', 'o', 'u'])

#boxplot = ax.boxplot(vocales)
plt.boxplot(vocales)

plt.show()


