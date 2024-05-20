import string
import random
def gen():
    s1 = string.ascii_uppercase #ASCII values for uppercase letters A-Z is 65-90

    s2 = string.ascii_lowercase #range for lowercase letters a-z is 97-122

    s3 = string.digits

    s4 = string.punctuation

    passlen = int(input("Enter the password length\n"))

    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)
gen()