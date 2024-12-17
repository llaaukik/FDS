
def Selection_Sort(marks):
    for i in range(len(marks)):

        
        min_idx = i #index 
        for j in range(i + 1, len(marks)): 
            if marks[min_idx] > marks[j]:
                min_idx = j

        
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])

 
def Bubble_Sort(marks):
    n = len(marks)
    
    for i in range(n - 1): #(1 2 3 4 5 ) 5-1=4 parant ch sort krnar karan 5 already sort aahe
        
        for j in range(0, n - i - 1):

             
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])

 

def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n") #[::-1]slicing that is used to reverse a list
                                 #sep seperte

 

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  #add kryala single element end la

print("The marks of",n,"students are : ")
print(marks)

flag=1; #flag=1 true boolen experssion 
while flag==1:
    print("\n---------------MENU---------------")
    print("1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Exit")
    ch=int(input("\n\nEnter your choice (from 1 to 3) : "))

    if ch==1:
        Selection_Sort(marks)
        a=input("\nDo you want to display top marks from the list (yes/no) : ")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")
            flag=0 #flag=0 false boolen experssion 

    elif ch==2: #elif (short form "else if)   "multiple if statements. 
        Bubble_Sort(marks)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")
            flag = 0

    elif ch==3:
        print("\nThanks for using this program!!")
        flag=0

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program!!")
        flag=0
        
        
        
        
#OUTPUT
#PS C:\Users\Aditya\OneDrive\Desktop\oop> python -u "c:\Users\Aditya\OneDrive\Desktop\26-Aaditya kulkarni\practical4.py"
#Enter number of students whose marks are to be displayed : 5
#Enter marks for 5 students (Press ENTER after every students marks): 
#89
#83
#7
#75
#91
#The marks of 5 students are : 
#[89, 83, 7, 75, 91]

#---------------MENU---------------
#1. Selection Sort of the marks
#2. Bubble Sort of the marks
#3. Exit


#Enter your choice (from 1 to 3) : 1
#Marks of students after performing Selection Sort on the list :
#7
#75
#83
#89
#91

#Do you want to display top marks from the list (yes/no) : yes
#Top 5 Marks are :
#91
#89
#83
#75
#7

#---------------MENU---------------
#1. Selection Sort of the marks
#2. Bubble Sort of the marks
#3. Exit


#Enter your choice (from 1 to 3) : 2
#Marks of students after performing Bubble Sort on the list :
#7
#75
#83
#89
#91

#Do you want to display top five marks from the list (yes/no) : yes
#Top 5 Marks are :
#91
#89
#83
#75
#7

#---------------MENU---------------
#1. Selection Sort of the marks
#2. Bubble Sort of the marks
#3. Exit


#Enter your choice (from 1 to 3) : 3

#Thanks for using this program!!        
        

 
