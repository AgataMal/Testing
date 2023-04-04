

'''def is_adult(age: int) -> bool:
    return age >=18

def test_is_adult():
    assert is_adult(20)
'''


def is_adult(age):
    if age >= 18:
        return True


print(is_adult(20))


def triangle_field(base, height) -> float:
    return 0.5 * base * height


def is_Weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 != 0 and n >= 6 and n < 20:
        print("Not Weird")
    else:
        print("Weird")


def is_leap(year):
    if year % 4 == 0: 
        if year %100==0:
            if year %400 == 0:
                return True
            return False
        return True
    return False

def capitalize(name:str)-> str:
    upper_names=[]
    white_space=False
    for i in name:    
        if i == " ":
            upper_names.append(i)
            white_space=True
            continue
        if i.isnumeric():
            upper_names.append(i)

        if i.islower():
            if len(upper_names)==0 or white_space:
                upper_names.append(i.upper())
            else:
                upper_names.append(i)
        white_space=False
    return "".join(upper_names)



