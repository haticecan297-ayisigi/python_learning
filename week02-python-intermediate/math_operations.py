def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def power(a, b):
    pow = 1
    if b > 0:
        for i in range(b):
            pow *= a
        print(pow)
    elif b == 0:
        print(pow)
    else:
        for i in range(-b):
            pow *= a
        print(1 / pow)

def multipy(a, b):
    print(a * b)

def divide(a, b):
    try:
        div = a / b
        print(div)
    except ZeroDivisionError:
        print("Sifira bolunmez!")
