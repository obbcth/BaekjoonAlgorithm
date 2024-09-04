n, b = map(int, input().split())
matrix = []

for _ in range(n):
    mat = list(map(int, input().split()))
    matrix.append(mat)


def mul_matrix(mat1, mat2):
    res = [[0]*len(mat1) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for z in range(len(mat1)):
                res[i][j] += mat1[i][z] * mat2[z][j] % 1000
    return res

def power(a, b):
    if b == 1:
        return a
    else:
        tmp = power(a, b // 2)
        if b % 2 == 0:
            return mul_matrix(tmp, tmp)
        else:
            return mul_matrix(mul_matrix(tmp, tmp), a)
        
result = power(matrix, b)

for _ in range(n):
    print(" ".join([str(i % 1000) for i in result[_]]))