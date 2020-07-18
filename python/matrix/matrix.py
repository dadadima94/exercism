class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(element) for element in line.split()]
                       for line in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [k[index - 1] for k in self.matrix]
