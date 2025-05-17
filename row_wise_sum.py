def row_wise_sum(matrix):
    row_sums = []

    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)

    return row_sums



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


row_sums = row_wise_sum(matrix)


print("Row-wise sums:")
for i, row_sum in enumerate(row_sums):
    print("Row", i + 1, "sum:", row_sum)
