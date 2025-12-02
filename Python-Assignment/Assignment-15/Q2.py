class Product:
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created.")

    def __del__(self):
        print("Product object destroyed.")

    def ShowProduct(self):
        print("Product ID   :", self.pid)
        print("Product Name :", self.pname)
        print("Price        :", self.price)
        print("Quantity     :", self.quantity)
        print("-" * 30)



p1 = Product()
p1.ShowProduct()


p2 = Product(201, "Laptop", 55000, 2)
p2.ShowProduct()
