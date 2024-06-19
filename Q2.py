class calculator():
   

    def __init__(self):
        print("enter 1 for add")
        print("enter 2 for subtraction")
        print("enter 3 for multiplication")
        print("enter 4 for division")
        self.add=0
        self.subtract=0
        self.multiply=1
        self.divide=0
        self.operator=0
        self.one=0
        self.two=0
        self.subtract1=0
    def getdata(self):
        self.operator=int(input("enter choice"))
    def operator1(self):
        b=[]
        z=[]
        if(self.operator==1):
            n=int(input("how many numbers you want to add"))
            for a in range(0,n):
                b.append(int(input("enter numbers")))
                self.add=self.add+b[a]
            print(self.add)

        elif(self.operator==2):
            n=int(input("how many numbers you want to subtract"))
            for a in range(0,n):
                z.append(int(input("enter numbers")))
            for c in range(1,n):
                self.subtract=self.subtract+z[c]
            self.subtract1=z[0]-self.subtract    
            print(self.subtract1)
                        
        elif(self.operator==3):
            n=int(input("how many numbers you want to multiply"))
            for a in range(0,n):
                b.append(int(input("enter numbers")))
                self.multiply=self.multiply*b[a]
            print(self.multiply)
        elif(self.operator==4):
            self.one=int(input("enter number"))
            self.two=int(input("enter number"))
            self.divide=self.one/self.two
            print(self.divide)
        else:
            print("wrong input")
d=calculator()
d.getdata()
d.operator1()

