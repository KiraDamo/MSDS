#Written by Kira Damo
#May 24th
#I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/elZzq8mGLGk

import math
import random
from A0701_KiraDamo import WarAndPeacePsuedoRandomNumberGenerator
    
class Point:
    'obtains points to be evaluated'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Ellipse:
    'creates ellipse information based on the focal points.'
    def __init__(self, f1, f2, major_axis_length):
        'initializes ellipse information'
        self.f1 = f1
        self.f2 = f2
        self.a = major_axis_length / 2
        
    def contains(self, p):
        d1 = math.dist([p.x, p.y], [self.f1.x, self.f1.y])
        d2 = math.dist([p.x, p.y], [self.f2.x, self.f2.y])
        return (d1 + d2) <= 2 * self.a


def computeOverlapOfEllipses(e1, e2, samples = 10000):
    
    prng = WarAndPeacePsuedoRandomNumberGenerator(42)

    xs = [e1.f1.x, e1.f2.x, e2.f1.x, e2.f2.x]
    ys = [e1.f1.y, e1.f2.y, e2.f2.y, e2.f2.y]
    buffer = max(e1.a, e2.a)

    min_x = min(xs) - buffer
    max_x = max(xs) + buffer
    min_y = min(ys) - buffer
    max_y = max(ys) + buffer

    count_inside_both = 0

    for _ in range(samples):
        x = prng.linear_combination() * (max_x - min_x) + min_x
        y = prng.linear_combination() * (max_y - min_y) + min_y
        point = Point(x,y)

        if e1.contains(point) and e2.contains(point):
            count_inside_both += 1

    bounding_area = (max_x - min_x) * (max_y - min_y)
    return bounding_area * (count_inside_both / samples)
    
p1 = Point(0,0)
p2 = Point(0,0)
e1 = Ellipse(p1, p2, 4)
e2 = Ellipse(p1, p2, 4)
overlap = computeOverlapOfEllipses(e1,e2)

print(overlap)

p3 = Point(5,0)
p4 = Point(6,1)
e3 = Ellipse(p3, p4, 4)
e4 = Ellipse(p3, p4, 10)
overlap2 = computeOverlapOfEllipses(e3,e4)

print(overlap2)
