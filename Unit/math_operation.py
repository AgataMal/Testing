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
