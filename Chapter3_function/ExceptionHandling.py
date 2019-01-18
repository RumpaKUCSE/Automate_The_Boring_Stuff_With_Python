def DividedBy(num):
    try:
        return 22/num
    except ZeroDivisionError:
        print('Error: Invalid Argument.')

print(DividedBy(2))
print(DividedBy(4))
print(DividedBy(0))
print(DividedBy(11))
