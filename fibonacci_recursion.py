def get_fibonacci(value):
    if value == 0 :
        return 0
    if value == 1:
        return 1

    return get_fibonacci(value-1) + get_fibonacci(value - 2)

print (get_fibonacci(5))
