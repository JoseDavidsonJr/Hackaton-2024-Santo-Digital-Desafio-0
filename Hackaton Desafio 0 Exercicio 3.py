def subconjunto(nums):
    conjunto = [[]]
    for i in nums:
        conjunto += [subconj + [i] for subconj in conjunto]
    return conjunto
array_string = input('Digite valores para o conjunto, separados por espaço (exemplo 1 23 45 6 7): ')
array_num = array_string.split()
array_num = [int(num) for num in array_num if num.isdigit() and 0 <= int(num) <= 9999]
resultado = subconjunto(array_num)
print(resultado)