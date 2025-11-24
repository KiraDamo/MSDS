#Written by Kira Damo
#Submitted May 3rd 2025
#I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/4W3EQTjIWkA

def human_pyramid(row, column):
    '''calculates the weight for each of the people in the pyramid'''
    
    if row == 0 and column == 0: # top of the pyramid
        return 0
    if row < 0 or column < 0 or column > row: #edges of the pyramid
        return 0
    #calculate the weight of the people in the middle of the pyramid
    weight = (human_pyramid(row-1, column-1)+human_pyramid(row-1, column))//2
    
    return 128 + weight
