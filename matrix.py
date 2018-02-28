from copy import copy, deepcopy

class Matrix:

    def __init__(self,size,list=None):
        self.size = size
        self.matrix = []
        if list != None:
            self.set_matrix(deepcopy(list))
        else:
            self.set_matrix_with_zero()


    def set_matrix(self,list):
        for i in list:
            self.matrix.append(i)

    def set_matrix_with_zero(self):
        zeros = [0]*self.size
        for i in range(self.size):
            self.matrix.append(deepcopy(zeros))

    def __iadd__(self, other):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] += other[i][j]
        return self


    def __add__(self, other):
        new_matrix = Matrix(self.size,None)
        new_matrix += self
        new_matrix += other
        return new_matrix

    def __imul__(self, other):
        if not isinstance(other,Matrix):
            for i in range(self.size):
                for j in range(self.size):
                    self.matrix[i][j] *= other
            return self
        else:
            copy_matrix = self.create_copy_Matrix()
            for i in range(self.size):
                for j in range(self.size):
                    s = 0
                    for k in range(self.size):
                        s += (copy_matrix.matrix[i][k]*other.matrix[k][j])
                    self.matrix[i][j] = s
            return self

    def __mul__(self, other):
        copy_matrix = self.create_copy_Matrix()
        copy_matrix *= other
        return copy_matrix

    def __imod__(self, other):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] %= other
        return self


    def __mod__(self, other):
        copy_matrix = self.create_copy_Matrix()
        copy_matrix %= other
        return copy_matrix

    def __ipow__(self, power):
        if power != 0:
            copy_matrix = self.create_copy_Matrix()
            for i in range(power - 1):
                self *= copy_matrix
        else:
            self.matrix = []
            self.set_matrix_with_zero()
            for i in range(self.size):
                self.matrix[i][i] = 1
        return self

    def __pow__(self, power):
        copy_matrix = self.create_copy_Matrix()
        copy_matrix **= power
        return copy_matrix

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        out = ""
        for i in self.matrix:
            out =  out + " ".join(str(x) for x in i) + "\n"
        return "{0}\n{1}".format(self.size, out)

    def __iter__(self):
        for i in range(self.size):
            for j in range(self.size):
                yield self.matrix[i][j]

    def create_copy_Matrix(other):
        copy_matrix = Matrix(other.size, None)
        copy_matrix.matrix = deepcopy(other.matrix.copy())
        return copy_matrix