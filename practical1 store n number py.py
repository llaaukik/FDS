
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999: #absent student
            sum+=listofmarks[i]
            count+=1
    avg=sum/count 
    print("Total Marks : ", sum)
    print("Average Marks : {:.2f}".format(avg))  #2f 2 decimal flaot

#<----------------------------------------------------------------------------------------------------->

# Function for Highest score in the test for the class

def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)

#<------------------------------------------------------------------------------------------------------>

# Function for Lowest score in the test for the class

def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

#<------------------------------------------------------------------------------------------------------->

# Function for counting the number of students absent for the test

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
            count+=1
    return(count)

#<------------------------------------------------------------------------------------------------------->

# Function for displaying marks with highest frequency
def maxFrequency(listofmarks):
    i=0
    Max=0
    print("Marks  |  Frequency") # | bitwise or 
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j,"    |  ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,Max)


#<------------------------------------------------------------------------------------------------------->

# Main function

marksinFDS=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    marksinFDS.append(marks)


average(marksinFDS)
print("Highest Score in Class : ", Maximum(marksinFDS))
print("Lowest Score in Class : ", Minimum(marksinFDS))
print("Number of Students absent in the test : ", absentcount(marksinFDS))
mark,fr = maxFrequency(marksinFDS)
print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))


#OUTPUT
#PS C:\Users\Aditya\OneDrive\Desktop\oop> python -u "c:\Users\Aditya\OneDrive\Desktop\26-Aaditya kulkarni\practical1.py"
#Enter total number of students : 5
#Enter marks of student 1 : 89
#Enter marks of student 2 : 98
#Enter marks of student 3 : 92
#Enter marks of student 4 : 95
#Enter marks of student 5 : 79
#Total Marks :  453
#Average Marks : 90.60
#Highest Score in Class :  98
#Lowest Score in Class :  79
#Number of Students absent in the test :  0
#Marks  |  Frequency
#89     |   1
#98     |   1
#92     |   1
#95     |   1
#79     |   1
#Highest frequency is of marks 89 that is 1