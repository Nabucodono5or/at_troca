'''
Usando o Thonny, escreva um programa em Python que
leia uma tupla contendo 3 números inteiros, (n1, n2, n3)
e os imprima em ordem crescente.
'''
tupla = (10, 5, 17)

def main(tupla):
    a, b, c = tupla
    if (a > b) :
        temp = b
        b = a
        a = temp
    if (a > c):
        temp = c
        c = a
        a = temp
    if (b > c):
        temp = c
        c = b
        b = temp

    novaTupla = (a, b, c)

    for x in novaTupla:
        print(x, end=" ")

main(tupla)
