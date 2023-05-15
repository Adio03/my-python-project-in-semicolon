def user_email(email):
    username = ""
    for name in email:
        if name != "@":
            username += name
        else:

            break

    return username


email = input("Enter your mail: \n")

print(user_email(email))
