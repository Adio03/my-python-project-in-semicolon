import random

face_one = 0
face_two = 0
face_three = 0
face_four = 0
face_five = 0
face_six = 0

for user_throws in range(1000):
    match random.randint(1, 6):
        case 1: face_one += 1

        case 2: face_two += 1

        case 3:  face_three += 1

        case 4: face_four += 1

        case 5: face_five += 1

        case 6: face_six += 1

print(f" face_one{face_one}")
print(f" face_two{face_two}")
print(f"face_three{face_three}")
print()