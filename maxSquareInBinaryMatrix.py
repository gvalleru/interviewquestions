
def print_matrix(m):
    for i in m:
        for j in i:
            print j,
        print ""
    print ""

def find_max_square(m):
    row = len(m)
    col = len(m[0])
    max_sq = 0
    max_row = 0
    max_col = 0

    for i in range(1, row):
        for j in range(1, col):
            if m[i][j] == 1:
                m[i][j] += min(m[i-1][j], m[i-1][j-1], m[i][j-1])
                if max_sq < m[i][j]:
                    max_sq = m[i][j]
                    max_row = i
                    max_col = j
                    #print max_sq, max_row, max_col

    for i in range(row):
        print m[i]
    print max_sq, max_row, max_col



binary_matrix = [[0, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1]]
#binary_matrix = [[0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 1, 1, 1]]

print_matrix(binary_matrix)
find_max_square(binary_matrix)