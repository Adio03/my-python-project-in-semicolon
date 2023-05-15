def isPrime(number):
    # Corner case
    if number <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
numbers = int(input())


# Driver Program to test above function
print("true") if isPrime(11) else print("false")
print("true") if isPrime(14) else print("false")
