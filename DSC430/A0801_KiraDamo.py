#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#Submitted May 31st
#https://youtu.be/CrnAlnBz1OU

import numpy as np

def karate_club():
    '''Program creates a summary of the karate club interactions'''

    #opens the txt file
    data = np.loadtxt('karate_club_interactions.txt')

    #matrix is symmetrical if transpose is equal to itself

    symmetry = np.array_equal(data, np.transpose(data))

    #verifies if data is symmetric.
    print('Is Karate Club data symmetric? {}'.format(symmetry))

    num_members = data.shape[0]
    print('number of members: ', num_members)
    
    #number of interactions
    interactions = np.sum(data, axis=1)
    for i in np.arange(num_members):
        print('Member {} had {} interaction(s)'.format(i+1, interactions[i]))
 
    #most and least active members
    min_interactions = np.min(interactions)
    max_interactions = np.max(interactions)
    
    least_active_members = np.where(interactions == min_interactions)[0]         
    most_active_members = np.where(interactions == max_interactions)[0]
    print('Least Active Members:')
    for i in least_active_members:
        print('Member {} with {} interactions'.format(i+1, interactions[i]))
    print('Most Active Members:')
    for i in most_active_members:
        print('Member {} with {} interactions'.format(i+1, interactions[i]))

    #finds if the most active and least active members interact
    interacted = False
    for low in least_active_members:
        for high in most_active_members:
            if data[low][high] > 0:
                interacted = True
                print('Member {} and Member {} did interact.'.format(low + 1, high + 1))
    if not interacted:
        print('None of the least and most active members interacted.')

    #average and std of interactions
    avg_interactions = np.mean(interactions)
    std_interactions = np.std(interactions)
    print('The average number of interactions: {}'.format(avg_interactions))
    print('The standard deviation of interactions: {}'.format(std_interactions))

karate_club()
