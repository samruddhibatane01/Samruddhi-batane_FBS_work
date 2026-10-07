class FBSstudent:
    stCount=0
    def __init__(self,frnno,name,batch):
        self.frnno=frnno
        self.name=name
        self.batch=batch
        FBSstudent.stCount+=1

    def getFrnNo(self):
        return self.frnno
    def setFrnNo(self,NewFrnNo):
        self.frnno=NewFrnNo

    def getName(self):
        return self.name
    def setName(self,NewName):
        self.name=NewName

    def getBatch(self):
        return self.batch
    def setBatch(self,NewBatch):
        self.batch=NewBatch

    def disply(self):
        print(f"FRN_No={self.frnno},Name={self.name},Batch={self.batch}")

class PlStudent(FBSstudent):
    def __init__(self, frnno, name, batch,cName):
        super().__init__(frnno, name, batch)
        self.cName=cName

    def disply(self):
        super().disply()
        print(f"CName={self.cName}")


f1=FBSstudent(21,"Samruddhi","June Python Data Science 2026")
f2=FBSstudent(22,'Saee','May Data Analytics 2026')
f3=PlStudent(23,'Mrunali','July2025','One8')
print(FBSstudent.stCount)
f3.disply()