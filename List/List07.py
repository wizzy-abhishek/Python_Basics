sub_list = int(input("Enter the number of sub-list you want in list\n"))
matrix = []

for i in range(sub_list):
    sub_matrix = []
    for j in range(sub_list):
        sublist_element = int(input(f"Enter the element for {i+1} and {j+1}: "))
        sub_matrix.append(sublist_element)
    matrix.append(sub_matrix)

print()

for i in matrix:
    print(i)

transpose_matrix = []

for i in range(sub_list):
    sub_list_mat = []
    for j in range(sub_list):
        sub_list_mat.append(matrix[j][i])
    transpose_matrix.append(sub_list_mat)

print("Transpose matrix\n")

for i in transpose_matrix:
    print(i)