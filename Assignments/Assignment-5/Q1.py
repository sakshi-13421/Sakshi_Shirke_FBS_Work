userid = "sakshi"
password = "1234"

for attempt in range(3):
    uid = input("Enter UserID: ")
    pwd = input("Enter Password: ")

    if uid == userid and pwd == password:
        print("Login Successful")
        break
    else:
        print("Invalid data! Try again.")

else:
    print("Too many failed attempts.")
