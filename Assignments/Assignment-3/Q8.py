
u= input("Enter User Id : ")
p= input("Enter Password : ")

if(u == 'sakshi' and p == 'sakshi123'):
    c=input("Enter Captcha")

    if(c == "1234"):
        print("Successfully Login")
    else:
        print("Failed Captcha")
else:
    print("Invalid")