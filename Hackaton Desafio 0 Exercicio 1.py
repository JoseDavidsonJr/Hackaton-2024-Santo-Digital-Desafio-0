def lista_asteriscos(n):
    return ["*" * i for i in range(1, n + 1)]
n = int(input('Digite um numero inteiro: '))
resultado = lista_asteriscos(n)
print(resultado)