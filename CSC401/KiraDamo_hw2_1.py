##Written By Kira Damo
#calculating grade average after dropping lowest grade

grades = eval(input('Please enter list of scores separated with commas: '))
if len(grades) == 1:
    gradesAverage=sum(grades)*2
    print('The rounded average of ' + str(len(grades)) + ' score is ' + str(round(gradesAverage)) + '%')
    print('The truncated average of ' + str(len(grades)) + ' score is ' + str(int(gradesAverage)) + '%')
else:
    gradesSum = (sum(grades)-min(grades)) * 2
    gradeAverage = gradesSum / (len(grades)-1)
    print('The average of ' + str(len(grades) - 1) + ' scores is ' + str(gradeAverage)+'%')
    print('The rounded average of ' + str(len(grades) - 1) + ' scores is ' + str(round(gradeAverage)) + '%')
    print('The truncated average of ' + str(len(grades) - 1) + ' scores is ' + str(int(gradeAverage)) + '%')

