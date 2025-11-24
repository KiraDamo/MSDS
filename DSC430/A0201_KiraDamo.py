#written By Kira Damo
def main():
    print('Welcome!/nThis program will display a stem and leaf plot for three files.')
    while True:
        filename1='StemAndLeaf1.txt'
        filename2='StemAndLeaf2.txt'
        filename3='StemAndLeaf3.txt'
        filename=['', filename1, filename2, filename3]

        choice=eval(input('Please choose a Stem and Leaf plot to display: 1, 2, or 3./Press 0 to exit. '))
        if choice == 0:
            print('Thank you. Goodbye')
            break
        elif choice in [1,2,3]:
            infile = open(filename[choice], 'r')
            linelist = infile.readlines()
            infile.close()
        else:
            print('Please enter a valid choice.')
            choice=eval(input('Please choose a Stem and Leaf plot to display: 1, 2, or 3./Press 0 to exit. '))
            
        plot={}
        for i in range ( 0, len(linelist) ):
            x = int(linelist[i].strip())
            stem = x // 10
            leaf = x % 10
            if stem in plot:
                plot[stem].append(leaf)
            else:
                plot[stem] = [leaf]

        for stem in sorted(plot.keys()):
            leaves = sorted(plot[stem])

            print('{} | {}'.format(stem, leaves))
            
        
            
