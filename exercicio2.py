

def main():
    n = int(input('Entre com um valor : '))
    total = 0
    for x in range(1, n + 1):
        if x % 2 == 0:
            total += x
    print("A soma total de valores pares até {} é : {} ".format(n, total))

if __name__ == '__main__':
    main()
