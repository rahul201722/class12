import random
class samyak:
    def __init__(self,x,y,z,a):
        self.__ad_no=0
        self.__name=""
        self.__class=""
        self.__fees=0
    def read_data(self,x,y,z,a):
        self.__ad_no=x
        self.__name=y
        self.__class=z
        self.__fees=a
    def display(self):
        print "admission.no=",self.__ad_no
        print "name=",self.__name
        print "class",self.__class
        print "fees",self.__fees
    def draws_nos(self):
        ad1=random.randint(1,5)
        ad2=random.randint(1,5)
        return ad1,ad2
    def display2(self):
        s1,s2=self.draws_nos()
        if self.__ad_no==s1 or self.__ad_no==s2:
            print "first person ad_no=",s1
            print "second person ad_no=",s2
            
        
l=[]
for i in range(1,6):
    x=raw_input("enter the name of student")
    x=samyak()
    
    adno=int(raw_input("enter the ad_no"))
    fees=int(raw_input("enter the fess"))
    clas=int(raw_input("entger the class"))
    samyak(adno,x,clas,fees)
    l.append(x)
    x.read_data()
