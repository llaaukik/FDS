

print("addition of matrix")
X = [[2,6,3],
    [5,9,7],
    [7,5,4]]

Y = [[9,8,3],
    [8,4,1],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
       
for r in result:
   print(r)
   
print("substraction for matrix") 
x = [[9,6,12],
    [7,11,2],
    [15,6,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
 
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] - Y[i][j]
for r in result :
   print(r)
print("transpose of matrix")
X = [[10,7],
    [4,3],
    [2,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
print("multiplication for matrix")  
X = [[11,6,7],
    [7,9,6],
    [5,12,7]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


#OUTPUT
#PS C:\Users\Aditya\OneDrive\Desktop\oop> python -u "c:\Users\Aditya\OneDrive\Desktop\26-Aaditya kulkarni\practical3.py"
#addition of matrix
#[11, 14, 6]
#[13, 13, 8]
#[11, 10, 13]
#substraction for matrix
#[-3, -2, 2]
#[-1, 2, 4]
#[3, 0, -5]
##transpose of matrix
#[10, 4, 2]
#[7, 3, 8]
#multiplication for matrix
#[119, 165, 92]
#[113, 149, 88]
#[125, 159, 104]