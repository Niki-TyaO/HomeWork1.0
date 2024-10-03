# def get_matrix(n, m, value):
#     return [[value for i in range(m)] for j in range(n)]
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            row.append(value)
        matrix.append(row)
        return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
