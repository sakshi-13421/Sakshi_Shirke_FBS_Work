cost_price = int(input("Enter a cost price of book="))
discount = int(input("Enter a discount price of book="))

discount = (discount / 100) * cost_price

selling_price = cost_price - discount

print(f"Selling price of the book is {selling_price}")