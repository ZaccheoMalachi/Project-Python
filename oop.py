class Car():
    def __init__(self,color,type,model,cylinder):
        self.color=color
        self.type=type
        self.model=model
        self.cylinder=cylinder
    def start(self):
        print('car is starting')
    def accelererate(self):
        print('car is accelerating')
    def reverse(self):
        print('car is reversing')
    def stop(self):
        print('car is stopping')
ford2021=Car('yellow','coupe','mustang',6)
bmw02=Car('orange','coupe','focus',4)
ford2021.start()
bmw02.stop()
if (ford2021.cylinder)>(bmw02.cylinder):
    print('ford2021 has more cylinder than bmw02')
else:
    print('bm02 has more cylinder than ford2021')