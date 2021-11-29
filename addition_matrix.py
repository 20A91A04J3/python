def create_matrix(rows,cols):
    matrix=[]
    for r in range(rows):
        row=[]
        for c in range(cols):
            v=int(input(f"enter element at row{r},column{c}:"))
            row.append(v)
        matrix.append(row)
    return matrix
rows=int(input('enter number of rows:'))
cols=int(input('enter number of columns:'))
print("\n enter elements into matrix 1:");
mat1=create_matrix(rows,cols)
print("\n enter elements into matrix 2:");
mat2=create_matrix(rows,cols)
def disp(matrix):
    for row in matrix:
        for val in row:
            print(f'{val:3d}',end="  ")
        print()
print('\n----mat(1)----')
disp(mat1)
print('\n----mat(2)----')
disp(mat2)
def mat_add(first,second):
    matrix=[]
    if len(first)==len(second)and len(first[0])==len(second[0]):
        matrix=[[first[i][j]+second[i][j] for j in range(len(first[0]))]for i in range(len(second[0]))]
        return matrix
res=mat_add(mat1,mat2)
print("\n---- ADDITION----")
disp(res)
