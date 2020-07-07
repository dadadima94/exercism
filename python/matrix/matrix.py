class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(element) for element in line.split()]
                       for line in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [l[index - 1] for l in self.matrix]
