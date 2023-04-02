import re


def email_validation(email: str) -> bool:
    return re.search("\\w+_\\w+@test.com", email) != None
