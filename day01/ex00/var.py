def my_var():
    value = 42
    print(value, "has a type", type(value))
    value = "42"
    print(value, "has a type", type(value))
    value = "quarante-deux"
    print(value, "has a type", type(value))
    value = 42.0
    print(value, "has a type", type(value))
    value = True
    print(value, "has a type", type(value))
    value = [42]
    print(value, "has a type", type(value))
    value = dict([(42, 42)])
    print(value, "has a type", type(value))
    value = (42,)
    print(value, "has a type", type(value))
    value = set()
    print(value, "has a type", type(value))

if __name__ == '__main__':
    my_var()