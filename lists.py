# lists = [1, 2, 3, 4, 5, 6]
# def square(n):
#     return n ** 2
#
# ans =list(map(square, lists))
# print(ans)

number =[5, 2, 8, 1, 9]
largest = number[0]
smallest = number[0]
for numbers in number:
    if numbers < largest:
        largest = number
    elif numbers > smallest:
        smallest = number
    print("largest number:", largest)
    print("small number:", smallest)