def sum_result(nums):
    result = 0
    for x in nums:
        result = x+result
        print(result)
    return result


def czy_liczba_pierwsza(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def reverse_list(lista):
    list = []
    dlugosc = len(lista)
    for x in reversed(range(dlugosc)):
        list.append(lista[x])
    return list

def reverse_list2(lista): # to do: zwalidować czy lista jest nieparzysta
    for i in range(len(lista)//2):
        temp=lista[i]
        lista[i]=lista[len(lista)-1-i]
        lista[len(lista)-1-i]=temp
    return lista    

def duplikaty(lista1, lista2):
    lista3 = []
    for i in lista1:
        for j in lista2:
            if i == j:
                lista3.append(i)
    return lista3


def srednia(lista_liczb: list) -> float:
    if len(lista_liczb) > 0:
        suma = 0
        for x in lista_liczb:
            suma += x
        return suma/len(lista_liczb)
    return None