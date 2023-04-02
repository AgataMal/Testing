import math


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


def reverse_list2(lista):
    if len(lista) % 2 == 0:
        raise ValueError("brak środkowego elementu")

    for i in range(len(lista)//2):
        temp = lista[i]
        lista[i] = lista[len(lista)-1-i]
        lista[len(lista)-1-i] = temp
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


def triangle_field(base, height) -> float:
    return 0.5 * base * height


def quadratic_function(a, b, c):
    delta = b**2-4*a*c
    if delta == 0:
        x1 = -b/2*a
        return [x1]

    elif delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        return [x1, x2]
    else:
        return None

def odd_even_counts(lista: list) -> list:
    even_list=[]
    odd_list=[]
    for i in lista:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
        
    return [len(even_list),len(odd_list)]

def even_counts(lista: list) -> list:
    even_counts=0
    for i in lista:
        if i%2==0:
            even_counts += 1
    return [even_counts, len(lista)-even_counts]

def how_many_letters(words: list) -> int:
    letters=0
    for word in words:
        letters += len(word)
    return letters

def how_many_vowels(words: list) -> int:
    vowel_letter=0
    vowels=("a", "u", "i", "e", "o")
    for word in words:
        for letter in word:
            if letter.lower() in vowels:
                vowel_letter+=1
    return vowel_letter




