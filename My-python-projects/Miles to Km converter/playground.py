def add(*arg):
    sum = 0
    for n in arg:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))
