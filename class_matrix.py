class Matrix(object):
    def __init__(self,mstring="",n=2,m=2):
        if mstring!="":
            self.data = self.makeMatrix(mstring)
            self.n = len(self.data)
            self.m = len(self.data[0])
        else:
            self.data = [[0 for _ in range(m)] for _ in range(n)]
            self.n = n
            self.m = m

    def set(self,i,j,value):
        self.data[i-1][j-1] = value

    def get(self,i,j):
        return self.data[i-1][j-1]

    def __str__(self):
        str =""
        for row in self.data:
            for x in row:
                str += "{:^5g}".format(x)
            str += "\n"
        return str

    def makeMatrix(self, mstring):
        """Converts and returns a list representation of a matrix from string of the form '1 2;3 4'"""
        return [[float(n) for n in r.split(" ")] for r in mstring.split(";")]

    def trace(self):
        """Returns the trace of self ie the sum of the diagonal elements"""
        assert self.n == self.m, "Trying to call trace on a non-square matrix"
        return sum([self.data[i][i] for i in range(self.n)])

    def transpose(self):
        """Returns a new matrix that is the transpose of self."""
        selfT = Matrix(n=self.m,m=self.n)
        selfT.data = [list(col) for col in zip(*self.data)]
        # alternatively you can use
        # selfT.data = [[row[i] for row in self.data] for i in range(self.m))]
        return selfT
        
    def getRow(self,i):
        """ Returns i-th row vector of matrix M with i starting from 1 """
        return self.data[i-1]

    def getColumn(self,j):
        """ Returns j-th column vector of matrix M with j starting from 1 """
        return [row[j-1] for row in self.data]
        # alternatively we could take the j-th row of the transpose
        # return self.transpose().getRow(j)
        
    def dot(self,M):
        """ Returns a matrix A that is the dot product of matrices self and M ie self.M = A """

        def vDot(u,v):
            """ Returns the dot product of 2 vectors.
            Added inside this Matrix method to ensure its availability for this method."""
            return sum([x*y for x,y in zip(u,v)])

        assert self.m == M.n, "Matrix dimensions mismatched when trying to perform dot product"

        A = Matrix(n=self.n, m=M.m)

        for i in range(1,self.n +1):
            row = self.getRow(i)

            for j in range(1,M.m +1):
                col = M.getColumn(j)
                A.set(i,j,vDot(row,col))
        return A
        
    def copy(self):
        """ Returns a new Matrix object that is a deep copy of self """
        A = Matrix(n=self.n,m=self.m)
        for i in range(1,self.n +1):
            for j in range(1,self.m +1):
                A.set(i,j,self.get(i,j))
        return A

    def contains(self, number):
        """ Returns True if one of the elements of self is equal to number """
        for i in range(1,self.n +1):
            for j in range(1,self.m +1):
                if self.get(i,j)==number:
                    return True
        else:
            return False
