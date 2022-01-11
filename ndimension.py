
import math
ertek = input('Adjon meg értékeket.')  
lista = ertek.split()
x = 0
def hosszusag(lista):
    for sor in lista:
        r = math.sqrt(int(sor) ** 2)
    x += r
    return x
hosszusag(lista)