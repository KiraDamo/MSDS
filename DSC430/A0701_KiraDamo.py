#Written by Kira Damo
#May 24th
#I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/1m4perd1yQU


import random

class WarAndPeacePsuedoRandomNumberGenerator:
    'creates a psuedo rng based on the indeces of war and peace txt file.'
    
    filename = 'war-and-peace.txt'
     
    def __init__(self, seed=None):
        'initializes initial index position (seed) and the second index position'
        self.seed = seed if seed is not None else 0
        self.position = self.seed
        self.load_text()
        
    def load_text(self):
        'opens the file in read mode'
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.text = file.read()
        self.text_length = len(self.text)
       
    def random_letter(self):
        '''if the second index position is greater than the length of the text,
        then the file should go back to the seed's position and add to it.'''

        char1 = self.text[self.position % self.text_length]
        char2 = self.text[(self.position + 100) % self.text_length]

        self.position = (self.position + 137) % self.text_length

        return 1 if char1 > char2 else 0

    def linear_combination(self):
        'calculates linear combination that is used as r'
        linear_combination = 0 
        for i in range(1,33):
            linear_combination += self.random_letter() * (1/(2**i))
        return linear_combination
        
if __name__ == "__main__":

    prng = WarAndPeacePsuedoRandomNumberGenerator(12345)

    results = []
    for i in range(0, 100000):
        results.append(prng.linear_combination())

    print('min:', min(results))
    print('max:', max(results))
    print('mean:',sum(results)/(len(results)))


        
