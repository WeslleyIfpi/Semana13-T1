def somaLista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def multiplicaLista(lista):
    multiplicacao = 1
    for i in range(len(lista)):
        multiplicacao *= lista[i]
    return multiplicacao

def main():
    lista = []
    for i in range(10):
        lista.append(int(input()))

    soma = somaLista(lista)
    multiplica = multiplicaLista(lista)

    print(lista)
    print(soma)
    print(multiplica)


if __name__ == '__main__':
    main()