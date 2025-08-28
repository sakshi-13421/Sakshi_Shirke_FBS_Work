import random
u = input("Enter User Id : ")
p = input("Enter Password : ")

if(u == 'sakshi' and p == 'sakshi123'):
    captcha=random.randint(1000,9999)
    print("Captcha : ", captcha)

    user_captcha = int(input("Enter the captcha : "))
    if(user_captcha == captcha):
        print("Successfully Login")
    else:
        print("Failed Captcha")
else:
    print("Invalid")