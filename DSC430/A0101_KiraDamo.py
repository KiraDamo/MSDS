#Written by Kira Damo
#Assignment 1 Question 1 due April 10th
#Submitted April 9th
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/xVdIcj-ljmE


def correctFile():
    'asks if file is the correct format'
    file_type=input("Is the assignment a single uncompressed .py file? yes/no ")
    file_type = file_type.lower()
    print(file_type)
    if file_type == "yes":
        return 1
    else:
        return 0
    
def name_and_date():
    'asks if the name and date are on the assignment'
    name_and_date=input("Does the assignment have the student's name and the date? yes/no ")
    name_and_date=name_and_date.lower()
    if name_and_date == "yes":
        return 1
    else:
        return 0
        
def honor_statement():
    'asks if honors statement is on the assignment'
    hnrstmnt="'I have not given or received any unauthorized assistance on this assignment'"
    honor_statement=input("Does assignment include the honors statement "+ hnrstmnt + ' yes/no ')
    honor_statement=honor_statement.lower()
    if honor_statement == "yes":
        return 1
    else:
        return 0
    
def yt_link():
    'asks if youtube link was provided'
    yt_link=input("Was an unlisted link of a 3-minute YouTube video explaining the code provided? yes/no ")
    yt_link=yt_link.lower()
    if yt_link == "yes":
        return 1
    else:
        return 0
            
def correctness():
    'asks to rate correctness on a scale of 0 to 10 and reassigns the answer as the point value.'
    correctness = -1
    while correctness < 0:
        correctness=eval(input("Out of 10 points, how correct is the code? "))
        if correctness >= 0 and correctness <= 10:
            return correctness 

def elegance():
    'asks to rate elegance on a scale of 0 to 10 and reassigns the answer as the point value.'
    elegance = -1
    while elegance < 0:
        elegance=eval(input("Out of 10 points, how elegant is the code (data structure selection, algorithm efficiency, function implementation, etc.)? "))
        if elegance >= 0 and elegance <= 10:
            return elegance

def hygiene():
    'asks to rate hygiene on a scale of 0 to 10 and reassigns the answer as the point value.'
    hygiene = -1
    hygiene=eval(input("Out of 10 points, how hygenic is the code (whitespace,doctstrings, etc.)? "))
    if hygiene >= 0 and hygiene <= 10:
        return hygiene

def discussion():
    'asks to rate discussion on a scale of 0 to 10 and reassigns the answer as the point value.'
    discussion = -1
    discussion=eval(input("Out of 10 points, how would you rate the quality of the discussion in the YouTube video? "))
    if discussion >= 0 and discussion <= 10:
        return discussion

def late(grade):
    'deducts points IF assignment was submitted late. Computes how many points get deducted based on hours late.'
    hours_late=eval(input("How many hours late was the assignment submitted? "))
    newgrade = (grade/40) * (1 - (hours_late*0.01)) #out of 40 points and deducts 1% for every hour late
    print("final assignment grade is " + str(round(newgrade*100)) + "%.")
    return newgrade
    

def computeGrade():
    '''calculates the grade IF all initial requirements are followed.
Then prompts if assignment was submitted late. Prints final grade'''
    if correctFile() == False:
        print("Requirements not met. Grade is zero.")
        return 0
    if name_and_date() == False:
        print("Requirements not met. Grade is zero.")
        return 0
    if honor_statement() == False:
        print("Requirements not met. Grade is zero.")
        return 0
    if yt_link() == False:
        print("Requirements not met. Grade is zero.")
        return 0

    p1 = correctness()
    p2 = elegance()   
    p3 = hygiene()
    p4 = discussion()

    rawgrade = p1 + p2 + p3 + p4

    late_submission=input("Did the student submit this assignment late? yes/no ")
    late_submission=late_submission.lower()
    if late_submission == "yes":
        grade = late(rawgrade)
    else:
        grade = rawgrade / 40
        print("final assignment grade is " + str(round(grade*100)) + "%.")
    return grade
    
computeGrade()


