#homework 5 problem 2
#written by Kira Damo

def budget(trans):
    print('Transactions:' + str(trans) + '. Value ' + str(sum(trans)))
    budget=[]
    while sum(trans) <= 0 and len(trans) != 0:
        trans.remove(min(trans))
        budget += trans
    if sum(trans) <= 0:
        print('Oops, looks bad, cannot be improved.')
    else:
        print('Budget: '+ str(trans) + '. Value ' + str(sum(trans)))

                    
#test cases
budget([-10,9,-50,20,-70,10,30,-30])
budget([-10,-50,-70,-30])
budget([-100,-200,-300,300])
budget([-10,-50,20,-70,30,-30])

