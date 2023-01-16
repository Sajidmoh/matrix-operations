print("MATRIX OPPERATIONS")
print("")

matrix1 = []
matrix2 = []
sumOfMatrix = []
subOfMatrix = []
matrixrows = int(input("how many rows in your matrix: "))
matrixcolumns = int(input("how many columns in your matrix: "))
print("")
print("Enter values for matrix 1")
for i in range(matrixrows):
    row = []
    for j in range (matrixcolumns):
        Inputs = int(input(f"matrix1: enter your number for position {i+1,j+1}:"))
        row.append(Inputs)
    matrix1.append(row)
print("")    
print("Enter values for matrix 2")    
for i in range(matrixrows):
    row2 = []
    for j in range (matrixcolumns):
        Inputs = int(input(f"matrix2: enter your number for position{i+1,j+1}: "))
        row2.append(Inputs)
    matrix2.append(row2)
    
#addition of matrix    
for i in range (matrixrows):
    row3 = []
    for n in range(matrixcolumns): 
        sum = matrix1[i][n] + matrix2[i][n]
        row3.append(sum)
    sumOfMatrix.append(row3)
    
#subtraction of matrix
for i in range (matrixrows):
    row3 = []
    for n in range(matrixcolumns): 
        sum = matrix1[i][n] - matrix2[i][n]
        row3.append(sum)
    subOfMatrix.append(row3)

print("")
print("matrix1")
for i in matrix1:
    print(i)
print("")    
print("matrix2")
for i in matrix2:
    print(i)
print("")
print("        sumOfMatrix")
print("this is the sum of matrix1 and matrix2")
for i in sumOfMatrix:
    print(i)
print("")    
print("        subOfMatrix")
print("this is the subtraction of matrix1 and matrix2")
for i in subOfMatrix:
    print(i)    