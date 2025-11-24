#homework 5 problem 1
#written by Kira Damo

#need accumulator loop
def evenRow(lst):
    sumNum = 0
    for i in range(0,len(lst)):
        sumNum = 0
        Test = []
        for j in range(0,len(lst[i])): 
            sumNum += lst[i][j]
            if sumNum%2 != 0:
                Test.append(False)
    if False in Test:
        return False
    else:
        return True
                

    
               
            


#test cases & solutions:
evenRow([[1,3],[2,4],[0,8]])
evenRow([[1,2,3],[3,4,7],[0,5,2]])
evenRow([[1,3,4],[2,4]])
evenRow([[1,2,3,4],[8,9],[-1,6,7],[8,0,1,1]])
