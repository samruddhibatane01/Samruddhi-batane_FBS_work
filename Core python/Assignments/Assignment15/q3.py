#Que1. Create a class Shirt with members as sid,sname,type(formal,etc),price and 
# size(small,large,etc).Add following methods-
# a)constructor (support both parameterized and parameterless)
# b)destructor
# c)showShirt

class Shirt:

    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def getSID(self):
        return self.sid
    def setSID(self,NewSID):
        self.sid=NewSID

    def getSName(self):
        return self.sname
    def setSName(self,NewSName):
        self.sname=NewSName

    def getType(self):
        return self.type
    def setType(self,NewType):
        self.type=NewType

    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice

    def getSize(self):
        return self.size
    def setSize(self,NewSize):
        self.size=NewSize

    def showShirt(self):
        print(f"SID={self.sid}\t Shirt_Name={self.sname}\t Type={self.type}\t Price={self.price}\t Size={self.size}")

    def __del__(self):
        print('Shirt Object Destroyed')
        
s1=Shirt(54,"Classic Blue","Formal",999,"Medium")
s1.showShirt()
