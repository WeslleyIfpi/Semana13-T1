def preencher(tamanhoLista, dado):
    lista = []
    for i in range(tamanhoLista):
        lista.append(dado)

    return lista
def preencher1N(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(i+1)

    return lista

def preencherUser(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(int(input()))

    return lista

def inverteLista(lista):
    listaInvertida = []
    for i in range(len(lista)-1, -1,-1):
        listaInvertida.append(lista[i])

    return listaInvertida


def main():
    tamanhoLista = int(input())

    lista0 = preencher(tamanhoLista, 0)
    lista1N = preencher1N(tamanhoLista)
    listaUser = preencherUser(tamanhoLista)
    listaUser2 = preencherUser(tamanhoLista)
    listaInvertida = inverteLista(listaUser2)

    print(lista0)
    print(lista1N)
    print(listaUser)
    print(listaInvertida)

if __name__ == '__main__':
    main()