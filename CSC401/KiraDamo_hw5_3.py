#Creating an nxn square with an x using asteriks
#written by Kira Damo

def squareDiagonals(n):
    for i in range(0,n):
        for j in range(0,n):
            if i == j or i == 0 or i == n-1 or i+1 == n-j:
                print('*', end=' ')
            elif j == 0 or j == n-1:
                print('*', end =' ')
            else: print(' ', end=' ')         
        print()
