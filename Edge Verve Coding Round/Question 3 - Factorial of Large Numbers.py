def factorial(number):
    temp = 1
    for i in range(1, number + 1):
        temp = temp * i
    return temp

number = raw_input("Enter a number:")

fact = factorial(int(number))

print fact
