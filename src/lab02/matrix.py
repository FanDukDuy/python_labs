def transpose(mat):
    if mat == []:
        return []
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            raise ValueError
    result = []
    for j in range(length):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        result.append(row)
    return result


def row_sums(mat):
    if mat == []:
        return []
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            raise ValueError
    result = []
    for row in mat:
        total = 0
        for x in row:
            total += x
        result.append(total)
    return result


def col_sums(mat):
    if mat == []:
        return []
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            raise ValueError
    result = []
    for j in range(length):
        total = 0
        for i in range(len(mat)):
            total += mat[i][j]
        result.append(total)
    return result

""" print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]])) """

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


""" print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]])) """