#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/RdL3x6BkX9g
#June 14th

import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, radius, year_length):
        self.radius = radius
        self.year_length = year_length

    def position(self, day):
        '''Finding the arc length and central angle of planet.
        Using trigonometry to find the vertical and horizontal
        components of each angle.'''
        a = 2 * math.pi * day / self.year_length
        x = self.radius * math.cos(a)
        x = round(x, 2)
        y = self.radius * math.sin(a)
        y = round(y, 2)
        return x, y

def distance(planet1, planet2, day):
    '''Finds the distance between the two planets using pythagorean theorem'''
    x1, y1 = planet1.position(day)
    x2, y2 = planet2.position(day)
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

def main():
    '''creating a simulation that runs for 1000 days and
    compute the distance between Earth
    to Mercury, Venus and Mars each day in two cases:
    (1) distances are stored exactly, (2) a noisy version
    of distances are stored. '''
    earth = Planet(9.3, 365)
    mercury = Planet(3.5, 88)
    venus = Planet(6.7, 225)
    mars = Planet(14.2, 687)

    earth_mercury = []
    earth_venus = []
    earth_mars = []
    nd_mercury = []
    nd_venus = []
    nd_mars = []

    s = 1.0
    
    for day in range(1,1001):
        d_mercury = distance(earth, mercury, day)
        earth_mercury.append(d_mercury)
        nd_mercury.append(d_mercury + np.random.normal(loc=0, scale=s))

        d_venus = distance(earth, venus, day)
        earth_venus.append(d_venus)
        nd_venus.append(d_venus + np.random.normal(loc=0, scale=s))

        d_mars = distance(earth, mars, day)
        earth_mars.append(d_mars)
        nd_mars.append(d_mars + np.random.normal(loc=0, scale=s))
    
    #plotting the normal graph
    plt.plot(earth_mercury, label='Mercury (original)', alpha=0.4)
    plt.plot(earth_venus, label='Venus (original)', alpha=0.4)
    plt.plot(earth_mars, label='Mars (original)', alpha=0.4)

    plt.axhline(np.mean(earth_mercury), label='Avg Mercury', linestyle='dashed', color='blue')
    plt.axhline(np.mean(earth_venus), label='Avg Venus', linestyle='dashed', color = 'orange')
    plt.axhline(np.mean(earth_mars), label='Avg Mars', linestyle='dashed', color = 'green')
    
    plt.title('Distance from Earth to Other Planets (original)')
    plt.xlabel('Days')
    plt.ylabel('Distance (CM)')
    plt.legend()
    plt.grid(True)
    plt.show()

    #plotting noisy graph
    plt.plot(nd_mercury, label='Mercury (noisy)', alpha=0.4)
    plt.plot(nd_venus, label='Venus (noisy)', alpha=0.4)
    plt.plot(nd_mars, label='Mars (noisy)', alpha=0.4)

    plt.axhline(np.mean(nd_mercury), label='Avg Mercury', linestyle='dashed', color='blue')
    plt.axhline(np.mean(nd_venus), label='Avg Venus', linestyle='dashed', color = 'orange')
    plt.axhline(np.mean(nd_mars), label='Avg Mars', linestyle='dashed', color = 'green')

    plt.title('Distance from Earth to Other Planets (noisy)')
    plt.xlabel('Days')
    plt.ylabel('Distance (CM)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"The distance between earth and mars on day 732 is {earth_mars[732]} CM")

    #8x8 Table
    planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    orbits = [3.5, 6.7, 9.3, 14.2, 48.0, 88.7, 178.4, 279.1]
    periods = [88, 225, 365, 687, 4333, 10759, 30687, 60190]
    planets = [Planet(r, T) for r, T in zip(orbits, periods)]

    matrix = np.zeros((8, 8))
    
    for i in range(0,8):
        for j in range(0,8):
            total = 0
            for day in range(1,365001):
                total += distance(planets[i], planets[j], day)
            avg = total / 365000
            matrix[i][j] = avg
            
    print('Avg Distance between planets')
    df = pd.DataFrame(matrix, index = planet_names, columns = planet_names)
    print(df.round(2))
    assert np.allclose(matrix, matrix.T) #checks if matrices are the same

    earth_row = matrix[planet_names.index('Earth')]
    closest_idx = np.argsort(earth_row)[1]

    print(f"The closest planet to earth is {planet_names[closest_idx]}")
    
