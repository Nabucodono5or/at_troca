
def potencia(a, b):
    # return a ** b
    # print(a ** b)
    total = 1
    if b == 0:
        return 1

    for x in range(1, b+1):
        total *= a
    return total

# print(potencia(3, 0))

def main():
    a = int(input('Entre com a base : '))
    b = int(input('Entre com a potência : '))
    resultado = potencia(a, b)
    print("Resultado de {} elevado a potência de {} é : {} .".format(a, b, resultado))

if __name__ == '__main__':
    main()
