#Developer:Ryan Tolentino
#Date: May 12,2016
""" The Purpose of this game to demonstrate the basic use of classes and how they are utlized in Python"""

class Hero:
    
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.posion = 0

    def eat(self,food):
        if(food=='shrimp'):
            if not(self.getHealth() >= 100):   
                self.health += 3
        elif(food=='trout'):
            if not(self.getHealth() >= 100):
                self.health += 5
        elif(food=='lobster'):
            if not(self.getHealth() >= 100):
                self.health += 12
        elif(food=='monkfish'):
            if not(self.getHealth() >= 100):
                self.health += 16
        elif(food=='shark'):
            if not(self.getHealth() >= 100):
                self.health += 20

    def poison(self,animal):
        
            if(animal == 'spider'):
                self.health -= 20
                if self.getHealth() <= 0:
                    print ('You are dead')
                    
            elif(animal == 'scorpion'):
                self.health -= 40
                if self.getHealth() <= 0:
                    print ('You are dead')
                    
            elif(animal == 'snake'):
                self.health -= 100
                if self.getHealth() <= 0:
                    print ('You are dead')
        

    def getHealth(self):
        return self.health

    def stillAlive(self):
        if self.health > 0:
            return True
        else:
            return False
            

zeus = Hero("Zeus")

print("Welcome to Varrock")
person = input("What is your name hero? ")
print("Please, come take a seat, get comfortable,here is our menue choose wisely....")
food = input("What would you like to eat? We have shrimp, trout, lobster, monkfish, shark,\nspider, scorpion, and even a snake:")
zeus.eat(food)
zeus.poison(food)
print("You have %s health"% zeus.getHealth())
print(zeus.stillAlive())
if zeus.stillAlive() == 1:
    print("Press enter to try a second dish or CTRL + C to exit")
else: print("Game Over");quit()
user_input= input()
print("You have %s health"% zeus.getHealth())
food = input("What would you like to eat? We have shrimp, trout, lobster, monkfish, shark,\nspider, scorpion, and even a snake:")
zeus.eat(food)
zeus.poison(food)
print("You have %s health"% zeus.getHealth())
print(zeus.stillAlive())
if zeus.stillAlive() == 1:
    print("Press enter to try a third and final dish or press CTRL + C to exit")
else: print("Game Over");quit()
user_input= input()
print("You have %s health"% zeus.getHealth())
food = input("What would you like to eat? We have shrimp, trout, lobster, monkfish, shark,\nspider, scorpion, and even a snake:")
zeus.eat(food)
zeus.poison(food)
print("You have %s health"% zeus.getHealth())
print(zeus.stillAlive())
if zeus.stillAlive() == 1:
    print("CONGRADULATIONS %s ,YOU HAVE WON!" %person) ; quit()
else: print("Game Over");quit()





    
    



