class Human():
    def __init__(self,name,height,weight,age,gender):
        self.name=name
        self.height=height
        self.weight=weight
        self.age=age
        self.gender=gender
    def speak(self):
        print('Person is speaking')
    def listen(self):
        print('Person is Listening')
    def eat(self):
        print('Person is eating')
    def walk(self):
        print('Person is walking')
    def run(self):
        print('Person is running')
jim=Human('Jim','170.1 cm','56.02 kg','15yo','male')
bob=Human('Bob','172.4 cm','57.0 kg','15yo','male')
jim.speak()
bob.listen()
