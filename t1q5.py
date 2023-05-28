def main():
    listaA = []
    listaB = []
    listaAB = []

    for i in range(25):
        listaA.append(int(input()))
    for j in range(25):
        listaB.append(int(input()))

    for k in range(25):
        listaAB.append(listaA[k])
        listaAB.append(listaB[k])

    print(listaA)
    print(listaB)
    print(listaAB)


if __name__ == '__main__':
    main()