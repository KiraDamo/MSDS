#Written By Kira Damo
#Submitted May 10
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/Jrrz18Ahlio

import random

class SixSidedDie:
    'This class represents a six sided die'

    def __init__(self):
        'initialize a starting value' #dice start at 1 not 0
        self.face = 1
        self.sides = 6
        
    def roll(self):
        'simulates rolling a die'
        self.face = random.randint(1, self.sides)

    def getFaceValue(self):
        'returns face value of die'
        return self.face

    def __repr__(self):
        'canonical string representation'
        return '{}({})'.format(self.__class__.__name__,self.face)

class TenSidedDie(SixSidedDie):
    'This class represents a ten sided die'

    def __init__(self):
        'initialize a starting value' 
        super().__init__()
        self.sides = 10

class TwentySidedDie(SixSidedDie):
    'This class represents a ten sided die'
    
    def __init__(self):
        'initialize a starting value' 
        super().__init__()
        self.sides = 20
        
class Cup:
    'This class represents dice in a cup'
    
    def __init__(self, count_six=1, count_ten=1, count_twenty=1):
        self.count_six = count_six
        self.count_ten = count_ten
        self.count_twenty = count_twenty #start the class with init
        self.SidedDie = []   
    
    def roll(self):
        'represents the rolling of each dice and adds them together'

        self.SidedDie=[]
        for i in range (self.count_six): 
            s=SixSidedDie()
            s.roll()
            self.SidedDie.append(s)
            
        for i in range(self.count_ten):
            t=TenSidedDie()
            t.roll()
            self.SidedDie.append(t)
            
        for i in range(self.count_twenty):
            w=TwentySidedDie()
            w.roll()
            self.SidedDie.append(w)
            
        return self.getSum()

    def getSum(self):
        'adds each of the faces of each of the die to the sum'
        return sum(die.getFaceValue() for die in self.SidedDie)

    def __repr__(self):
        return 'Cup({},{},{})'.format(self.SidedDie[0], self.SidedDie[1], self.SidedDie[2])
