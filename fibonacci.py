a = 0
b = 1

number_of_numbers = int(input("How many Fibonacci numbers would you like to generate? "))

for i in range(number_of_numbers):
    print(a, end=" ")
    c = a
    a = b
    b = c + b