CP=int(input("Enter a Cost Price : "))
SP=int(input("Enter a Selling Price : "))

if(SP > CP):
    profit=SP - CP
    print(f"Profit : ", profit)
elif(SP < CP):
    loss=CP - SP
    print(f"Loss : ", loss)
else:
    print(f"No Profit or Loss")