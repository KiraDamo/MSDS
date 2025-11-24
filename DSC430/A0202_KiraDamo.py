#Written by Kira Damo
#Assignment 2 Question 2 Due April 17th
#submitted April 17th
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/iAODVPfP4nU

def print_intro():
    print('Hello! In this program, we will create a stem and leaf plot for 3 files.')
    print('''Based on the user's decision, a stem and leaf plot will be displayed for that file.\n''')

def get_data(n):
    '''gets the data based on the choice of the user. the choice will select the filename to read'''
    filename1='StemAndLeaf1.txt'
    filename2='StemAndLeaf2.txt'
    filename3='StemAndLeaf3.txt'
    filename=['', filename1, filename2, filename3] ##choices are 1,2,3 so index 0 is blank. 

    infile = open(filename[n], 'r')
    data = infile.readlines()
    infile.close()

    return data

def stem_and_leaf_plot(data):
    '''adds data to dictionary where stem is key and leaf are values'''  
    plot={}
    for i in range ( 0, len(data)):
        x = int(data[i].strip())
        stem = x // 10
        leaf = x % 10
        if stem in plot:
            plot[stem].append(leaf)
        else:
            plot[stem] = [leaf]

    for stem in sorted(plot.keys()):
        leaves = sorted(plot[stem]) #sorts the stems and leaves
        print('{} | {}'.format(stem, leaves)) #prints each line as a stem and life plot

def main():
    '''greets user and gets their choice of which file to read. If user chooses 0, the loop will break.
If user does not enter 0, 1, 2, or 3, loop will rerun and ask for a valid choice.'''    
    print_intro()
    while True:
        choice=eval(input('Please choose a Stem and Leaf plot to display: 1, 2, or 3.\nPress 0 to exit. '))
        if choice in [1,2,3]:
            data = get_data(choice)
            plot = stem_and_leaf_plot(data)
        elif choice == 0:
            print('Thank you. Goodbye')
            break
        else:
            print('Please enter a valid choice.')
    return

main()
        
        
