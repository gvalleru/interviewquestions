class MatrixSpiral:

    def __init__(self, matrix):
        self.matrix = matrix

    def print_spiral(self):
        r = len(self.matrix)
        c = len(self.matrix[0])
        out = []

        s_r = 0
        e_r = r - 1

        s_c = 0
        e_c = c - 1

        while s_r <= e_r or s_c <= e_c:
            for i in range(s_c, e_c + 1):
                out.append(self.matrix[s_r][i])
            s_r += 1

            for i in range(s_r, e_r + 1):
                out.append(self.matrix[i][e_c])
            e_c -= 1

            for i in range(e_c, s_c - 1, -1):
                out.append(self.matrix[e_r][i])
            e_r -= 1

            for i in range(e_r, s_r - 1, -1):
                out.append(self.matrix[i][s_c])
            s_c += 1

        return out[0:r*c]


if __name__ == "__main__":
    # input_ = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    input_ = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    x = MatrixSpiral(input_)
    print x.print_spiral()
