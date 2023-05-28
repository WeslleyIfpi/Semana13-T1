def preencherUser(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(float(input()))

    return lista


def preencherUserLetra(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(input())

    return lista

def inverteLista(lista):
    listaInvertida = []
    for i in range(len(lista)-1, -1,-1):
        listaInvertida.append(lista[i])

    return listaInvertida

def calculaMedia(lista):
    somatorio = 0
    for i in range(len(lista)):
        somatorio += lista[i]

    return somatorio/len(lista) if len(lista) > 0 else 0

def contaVogais(listaLetras):
    totalVogais = 0
    for letra in range(len(listaLetras)):
        if (listaLetras[letra]).lower() in ['a', 'e','i','o','u']:
            totalVogais += 1
    
    return totalVogais

def retornaConsoantes(listaLetras):
    consoantes = []
    for i in range(len(listaLetras)):
        if (listaLetras[i]).lower() not in ['a', 'e','i','o','u']:
            consoantes.append(listaLetras[i].strip())
    
    return consoantes

def main():

    quantidade = int(input())

    lista = preencherUser(quantidade)
    listaInvertida = inverteLista(lista)
    notas = preencherUser(quantidade)
    media = calculaMedia(notas)
    listaLetras = preencherUserLetra(quantidade)
    quantidadeVogais = contaVogais(listaLetras)
    listaConsoantes = retornaConsoantes(listaLetras)

    print(listaInvertida)
    print(notas)
    print(f'{media:.1f}') if media > 0 else print('SEM NOTAS')
    print(quantidadeVogais)
    print(listaConsoantes)

if __name__ == '__main__':
    main()