print("Enter 5 product of prise")
p1=int(input("Enter a Product1 : "))
p2=int(input("Enter a Product2 : "))
p3=int(input("Enter a Product3 : "))
p4=int(input("Enter a Product4 : "))
p5=int(input("Enter a Product5 : "))

total = p1 + p2 + p3 + p4 + p5

if(total > 0):
    gst = total * 0.18
    final = total + gst
    print("Subtotal : ", total)
    print("GST 18% :", gst)
    print("Total Bill : ", final)
else:
    print("No product purchase")
