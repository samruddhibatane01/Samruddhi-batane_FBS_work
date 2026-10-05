#Que1. Create a class Product with members as pid,pname,price and quantity.
# Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showProduct
# d)add static member discount
# e)Provide methods for applying discount on price of product

class Product:
    
    discount=10

    def __init__(self,pid=0,pname="",price=0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def getPID(self):
        return self.pid
    def setPID(self,NewPID):
        self.pid=NewPID

    def getPName(self):
        return self.pname
    def setPName(self,NewPName):
        self.pname=NewPName

    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice

    def getQuantity(self):
        return self.quantity
    def setQuantity(self,NewQuantity):
        self.quantity=NewQuantity

    def showProduct(self):
        print(f"PID={self.pid}\t Product_Name={self.pname}\t Price={self.price}\t Quantity={self.quantity}")

    def applyDiscount(self):
            discount_amount=self.price*Product.discount/100
            self.price=self.price-discount_amount


    def __del__(self):
        print('Product Object Destroyed')
        
p1=Product(564,"Washing Machine",19000,2)
p2=Product()
print('Before Discount')
p1.showProduct()
p1.applyDiscount()
print('After Discount')
p1.showProduct()

p2.showProduct()