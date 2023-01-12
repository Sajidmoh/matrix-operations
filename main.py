matrix1 = []
matrix2 = []
sumOfMatrix = []
subOfMatrix = []
for i in range(2):
    row = []
    for i in range (2):
        Inputs = int(input("enter your number: "))
        row.append(Inputs)
    matrix1.append(row)
for i in range(2):
    row2 = []
    for i in range (2):
        Inputs = int(input("enter your number: "))
        row2.append(Inputs)
    matrix2.append(row2)
    
#addition of matrix    
for i in range (2):
    row3 = []
    for n in range(2): 
        sum = matrix1[i][n] + matrix2[i][n]
        row3.append(sum)
    sumOfMatrix.append(row3)
    
#subtraction of matrix
for i in range (2):
    row3 = []
    for n in range(2): 
        sum = matrix1[i][n] - matrix2[i][n]
        row3.append(sum)
    subOfMatrix.append(row3)


print(matrix1)
print(matrix2)
print(sumOfMatrix)      
print("sumOfMatrix")
for i in sumOfMatrix:
    print(i)
print("subOfMatrix")
for i in subOfMatrix:
    print(i)    