def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result



def print_matrix(matrix):
    for row in matrix:
        print(row)



matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]


result = multiply_matrices(matrix1, matrix2)


if result is not None:
    print("Matrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)
    print("\nProduct of the matrices:")
    print_matrix(result)
else:
    print("Matrices cannot be multiplied. Number of columns in matrix1 must be equal to the number of rows in matrix2.")
