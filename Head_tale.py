import random
head = 0
tail = 0
for head_tail in range(100):
    match random.randint(1, 2):
        case 1: head += 1
        case 2: tail += 1


print(f" head {head}")
print(f"tail {tail}")
