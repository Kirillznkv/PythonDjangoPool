def printIntFromFile(fileName):
    with open(fileName, 'r') as f:
        fstr = f.read()
    numbers = fstr.split(',')
    for num in numbers:
        print(num.strip())


if __name__ == '__main__':
    printIntFromFile("./numbers.txt")