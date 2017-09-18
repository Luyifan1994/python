import string, random

def generate(a, b, c):
    field = string.letters + string.digits
    for j in range(c):
        part = []
        for i in range(a):
            part.append("".join(random.sample(field, b)))
        index = "-".join(part)
        print index

generate(5, 6, 6)
