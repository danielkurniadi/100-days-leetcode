"""
"""


def maximum_rectangle_area(matrix):
    if not matrix or not matrix[0]: return 0

    N = len(matrix)
    M = len(matrix[0])
    
    integral = integral_matrix(matrix)
    largest_area = 0
    
    print(integral)

    for i1 in range(1, N+1):
        for j1 in range(1, M+1):
            for i2 in range(i1, N+1):
                for j2 in range(j1, M+1):
                    area = integral[i2][j2] + integral[i1-1][j1-1] \
                        - integral[i1-1][j2] - integral[i2][j1-1]
                    # check area doesn't have missing hole
                    if area == (j2-j1+1) * (i2-i1+1):
                        print((i1,j1),(i2,j2), area)
                        largest_area = max(area, largest_area)
    return largest_area


def integral_matrix(matrix):
    N = len(matrix)
    M = len(matrix[0])

    intg_matrix = [[0 for _ in range(M+1)]
                   for _ in range(N+1)]

    # initialise integral
    intg_matrix[1][1] = matrix[0][0]
    for i in range(1, N+1):
        intg_matrix[i][1] = intg_matrix[i-1][1] + matrix[i-1][0]
    for j in range(1, M+1):
        intg_matrix[1][j] = intg_matrix[1][j-1] + matrix[0][j-1]

    # integralisation
    for i in range(1, N+1):
        for j in range(1, M+1):
            intg_matrix[i][j] = intg_matrix[i-1][j] + intg_matrix[i][j-1] \
                                - intg_matrix[i-1][j-1] + matrix[i-1][j-1]

    return intg_matrix


if __name__ == "__main__":
    # TEST CASE 1
    matrix = [[1,0,1,0,0],
              [0,0,1,0,1],
              [0,0,1,0,1],
              [1,0,0,0,0]]
    largest_area = maximum_rectangle_area(matrix)
    print(largest_area)
