def menor_dif_absol(array):
    if len(array) < 2:
        return []
    menor_dif = float('inf')
    array_dif = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            dif = abs(array[j] - array[i])
            if dif < menor_dif:
                menor_dif = dif
                array_dif = [(array[i], array[j])]
            elif dif == menor_dif:
                array_dif.append((array[i], array[j]))
    return array_dif

array_string = input('Digite valores para a array, separados por espaço (exemplo 1 23 45 6 7): ')
array_num = array_string.split()
array_num = [int(num) for num in array_num if num.isdigit() and 0 <= int(num) <= 9999]
resultado = menor_dif_absol(array_num)
for par in resultado:
    print(f'Par: {par[0]}, {par[1]}')