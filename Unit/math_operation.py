def sum_result(nums):
    result = 0
    for x in nums:
        result = x+result
        print(result)
    return result


def czy_liczba_pierwsza(n):
    if n==1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def reverse_list(dupa):
    list=[]
    dlugosc=len(dupa)
    for x in reversed(range(dlugosc)):
        list.append(dupa[x])
    return list

def duplikaty(lista1,lista2):
    lista3=[]
    for i in lista1:
        for j in lista2:
            if i==j:
                lista3.append(i)
    return lista3