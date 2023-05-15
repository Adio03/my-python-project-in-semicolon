def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz "
    if n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"

for index in range(1, 101):
    print(fizzbuzz(index))

