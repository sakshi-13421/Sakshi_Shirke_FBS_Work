amount = int(input("Enter amount: "))

print("Minimum notes required:")

while amount > 0:
    if amount >= 2000:
        print("2000 :", amount // 2000)
        amount %= 2000
    elif amount >= 500:
        print("500 :", amount // 500)
        amount %= 500
    elif amount >= 200:
        print("200 :", amount // 200)
        amount %= 200
    elif amount >= 100:
        print("100 :", amount // 100)
        amount %= 100
    elif amount >= 50:
        print("50 :", amount // 50)
        amount %= 50
    elif amount >= 20:
        print("20 :", amount // 20)
        amount %= 20
    elif amount >= 10:
        print("10 :", amount // 10)
        amount %= 10
    elif amount >= 5:
        print("5 :", amount // 5)
        amount %= 5
    elif amount >= 2:
        print("2 :", amount // 2)
        amount %= 2
    else:
        print("1 :", amount)
        break
