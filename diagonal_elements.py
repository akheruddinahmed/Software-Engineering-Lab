def print_principal_diagonal(matrix):
    if not matrix:
        print("Matrix is empty.")
        return

    diagonal_elements = []
    min_dim = min(len(matrix), len(matrix[0]))

    for i in range(min_dim):
        diagonal_elements.append(matrix[i][i])

    print("Principal diagonal elements:", diagonal_elements)



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


print_principal_diagonal(matrix)
