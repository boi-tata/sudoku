class SudokuException(Exception):
    pass


class InvalidInput(SudokuException):
    pass


class InvalidValue(SudokuException):
    pass


class Sudoku:
    """Class thats represent a Sudoku puzzle."""

    def __init__(self, source:str):
        with open(source) as f:
            raw = f.read()
        
        # Generating matrix
        matrix = [x.split() for x in raw.splitlines() if len(x)]
        self.dimension = len(matrix)
        
        # Item 2.6
        if not self.dimension:
            raise InvalidInput('Empty input')
        
        # Items 3.1 e 3.2
        f = lambda row: len(row) != self.dimension
        if any(map(f, matrix)):
            raise InvalidInput('Inconsistent lines')
        
        # Converting elements to integers
        self._matrix = [[int(y) for y in x] for x in matrix]
        
        # Items 2.3 e 3.3
        f = lambda x: self.dimension< x < 0
        if any(any(map(f, row)) for row in self._matrix):
            raise InvalidInput('Input have one or more invalid numbers')
        
        # Checking if matrix has submatrix. The value represents the size
        # of each submatrix
        from math import sqrt

        temp = sqrt(self.dimension)
        self.has_submatrix = int(temp) if (temp == int(temp)) else 0

    
    def row(self, index:int) -> list:
        """Return a list thats represents a row from given `index`."""
        return self._matrix[index]


    def column(self, index:int) -> list:
        """Return a list thats represents a column from given `index`."""
        return [row[index] for row in self._matrix]

    
    def submatrix(self, x:int, y:int) -> list:
        """Return a list thats represents a submatrix thats contains the
        element from given index (x, y). If matrix hasn't submatrix, return
        `None`."""
        if not self.has_submatrix:
            return

        get_start = lambda n: (n // self.has_submatrix) * self.has_submatrix
        
        # Getting rows thats compound the submatrix
        st = get_start(x)
        rows = self._matrix[st:(st + self.has_submatrix)]
        
        # Removing columns thats outside submatrix
        st = get_start(y)
        sub = [row[st:(st + self.has_submatrix)] for row in rows]

        # Flatten submatrix
        return [i for row in sub for i in row]
    
    
    def set(self, x:int, y:int, value:int, only_check=False) -> bool:
        """If is possible, set `value` in given index (x, y) and return
        `True`, else return `False`. If `only_check` is `True`, won't
        assign `value` to the index."""
        if self.dimension < value < 0:
            raise InvalidValue('Value not allowed')
        
        if value:
            # Item 1.1
            if value in self.row(x):
                return False

            # Item 1.2
            if value in self.column(y):
                return False

            # Item 3.4
            if self.has_submatrix and value in self.submatrix(x, y):
                return False

        if not only_check:
            self._matrix[x][y] = value
        return True

    
    def get(self, x:int, y:int) -> int:
        """Retrieves value in index (x, y)."""
        return self._matrix[x][y]


    def solve_bf(self):
        """Solves the puzzle by brute force."""
        # Iterate over matrix
        for x in range(self.dimension):
            for y in range(self.dimension):

                # Skip not empty index
                if self.get(x, y):
                    continue

                # Try to fit a number in index
                for value in range(1, self.dimension + 1):

                    # If not fit, try next number
                    if not self.set(x, y, value):
                        continue

                    # Try to solve the new state of matrix. If `True` is
                    # returned, so a solution has been finded. Else, the actual
                    # state is part of wrong solution, and next number is tried.
                    if self.solve():
                        return True
                
                # If no number fits, previous state isn't part of solution. So,
                # any change on actual state is undone, and we back to modify
                # previous state
                self.set(x, y, 0)
                return False
        
        # When reached this line, the matrix has been filled, and a solution
        # has been encoutered
        return True


    def __str__(self):
        return '\n'.join(map(lambda l: ' '.join(map(str, l)), self._matrix))


    def __repr__(self):
        d = self.dimension
        return 'Sudoku(%dx%d)' % (d, d)