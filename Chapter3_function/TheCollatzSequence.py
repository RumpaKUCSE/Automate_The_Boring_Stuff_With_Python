def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return number*3 + 1
try:
    number = int(input('Enter number:'))
    while 1:
        print(collatz(number))
        number = collatz(number)
        if number == 1:
            break
except ValueError:
    print('Enter integer :')
