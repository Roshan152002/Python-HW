class Parent:
    def __init__(self):
        self.surname = 'madle'
        self.name = 'nagnath'
        print(f'{self.surname} {self.name}')

    def land(self):
        print('fathers land and property')
    
class Son(Parent):
    def __init__(self):
        self.name = 'roshan'
        print(f'{self.name}')
    

s = Son()
s.land()

