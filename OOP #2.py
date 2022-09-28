class PlayerChar:
    membership = True
    def __init__(self, name, age):
        if (self.membership):
            self.name = name #attributes
            self.age = age
        
        
    def say(self, hello):
       
        print('say')
        return(f'my name is {self.name}')

    @classmethod
    def adding_things(cls,num1,num2):
        return cls('teddy', num1 + num2)

player1 = PlayerChar('Randy', 21)
player2 = PlayerChar('Robert', 44)
player2.attack = 50
player3 = PlayerChar.adding_things(2,3)

# print(player1.say('hello'))
print(player1.age, player1.name)
# print(player2.name)
# print(player2.attack)
# help(player1) #blueprint
print(player3.age)

 