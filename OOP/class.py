class Human:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


human1 = Human('Abhishek', 21)
human1.friend = 'Gargi'

print(human1.__getattribute__('friend'))