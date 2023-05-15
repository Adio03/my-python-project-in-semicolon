
names = []
for i in range(1, 10):
    print("enter the names")
    name = input()
    i = name
    if len(name) < 10 and len(name) != 0:
        names.append(name)
    else:
        print("enter another name ")

print(names)
