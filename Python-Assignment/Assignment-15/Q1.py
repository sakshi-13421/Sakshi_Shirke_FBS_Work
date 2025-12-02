class Book:
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object created.")

    def __del__(self):
        print("Book object destroyed.")

    def ShowBook(self):
        print("Book ID     :", self.bid)
        print("Book Name   :", self.bname)
        print("Price       :", self.price)
        print("Author Name :", self.author)
        print("-" * 30)


b1 = Book()   
b1.ShowBook()

b2 = Book(101, "Python Programming", 450, "Guido van Rossum")  
b2.ShowBook()
