def ehPar(numero):
    return numero % 2 == 0

def main():
    lista = []
    listaPares = []
    listaImpares = []

    for i in range(20):
        entrada = int(input())
        lista.append(entrada)
        if ehPar(entrada):
            listaPares.append(entrada)
        else:
            listaImpares.append(entrada)

    print(lista)
    print(listaPares)
    print(listaImpares)

if __name__ == '__main__':
    main()