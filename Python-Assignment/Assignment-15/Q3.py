class Shirt:
    def __init__(self, sid=None, sname=None, stype=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype    
        self.price = price
        self.size = size      
        print("Shirt object created.")

    def __del__(self):
        print("Shirt object destroyed.")

    def ShowShirt(self):
        print("Shirt ID    :", self.sid)
        print("Shirt Name  :", self.sname)
        print("Type        :", self.stype)
        print("Price       :", self.price)
        print("Size        :", self.size)
        print("-" * 30)


s1 = Shirt()
s1.ShowShirt()

s2 = Shirt(301, "Peter England", "Formal", 1200, "Large")
s2.ShowShirt()
