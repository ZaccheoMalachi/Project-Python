class Phone:
    def __init__(self,type,color,price):
        self.type=type
        self.color=color
        self.price=price
    def call(self,num):
        print(self.type,'is calling',num)
    def message(self,num,message):
        print(self.type,'is sending a message','\"',message,'\"','to',num)
    def start(self):
        print(self.type,'is starting')
    def shutting(self):
        print(self.type,'is shutting down')
class Android(Phone):
    def openplaystore(self):
        print(self.type,'is opening Playstore')
    def start(self):
        print(self.type,'is starting')
class Iphone(Phone):
    def openapplestore(self):
        print(self.type,'is opening Applestore')
    def start(self):
        print(self.type,'is starting')
nokia3310=Phone('Nokia3310','grey','$13,25')
iPhone14=Iphone('IPhone14','red','$2769,00')
oPPOFindX5Pro=Android('OPPO Find X5 Pro','black','$1059,95')
nokia3310.message(911,'Help Me')
iPhone14.message(911,'Help Me')
oPPOFindX5Pro.message(112,'Help Me')