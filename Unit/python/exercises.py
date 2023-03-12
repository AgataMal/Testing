

'''def is_adult(age: int) -> bool:
    return age >=18

def test_is_adult():
    assert is_adult(20)
'''
def is_adult(age):
    if age>=18:
        return True
print (is_adult(20))


def triangle_field(base, height)->float:
    return 0.5 * base * height
