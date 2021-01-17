
def deepcopy(grid):
    grid2 = [x.copy() for x in grid]
    return grid2


# get the number of the tile that position i,j belong to
def tile(i,j):
    return (i//3)*3+j//3



# get the next index of the grid, row-major order
def next(i,j):
    if i == 8 and j == 8: return -1,-1
    if j == 8: return i+1,0
    return i,j+1

# this class stores the relevant data about the sudoku and provides methods to
# solve it
class Grid:
    def __init__(self,setup_grid):
        # hash sets for every row, col and tile
        self.defaultGrid = setup_grid
        self.rows = [set() for i in range(9)]
        self.cols = [set() for i in range(9)]
        self.tiles = [set() for i in range(9)]
        self.defaults = set()
        # add the given numbers
        for i in range(9):
            for j in range(9):
                el = setup_grid[i][j]
                if el != 0:
                    self.rows[i].add(el)
                    self.cols[j].add(el)
                    self.tiles[tile(i,j)].add(el)
                    self.defaults.add((i,j))

        self.grid = deepcopy(setup_grid)

    # set grid back to initial state
    def restoreDefault(self):
        self.grid = deepcopy(self.defaultGrid)

    # check if a number is currently allowed at position i,j
    def check(self,num,i,j):
        return num not in self.rows[i] and num not in self.cols[j] and num not in self.tiles[tile(i,j)]

    # change value at i,j to num
    def put(self,i,j,num):
        self.remove(i,j)
        self.add(i,j,num)

    # add number at pos i,j
    def add(self,num,i,j):
        self.rows[i].add(num)
        self.cols[j].add(num)
        self.tiles[tile(i,j)].add(num)
        self.grid[i][j] = num

    # remove num at i,j
    def remove(self,i,j):
        num = self.grid[i][j]
        if num in self.rows[i]:
            self.rows[i].remove(num)
        if num in self.cols[j]:
            self.cols[j].remove(num)
        if num in self.tiles[tile(i,j)]:
            self.tiles[tile(i,j)].remove(num)
        self.grid[i][j] = 0

    # recursively fill in the sudoku, starting at position i,j
    def solveFrom(self,i,j):
        # if we filled in every field, we solved the sudoku
        if i == -1 and j == -1: return True

        # if field already contains a (given) number, just proceed to next one
        if self.grid[i][j] != 0:
            return self.solveFrom(*next(i,j))

        # put the allowed numbers from 1 to 9 one by one in the current field
        # check recursively if this leads to a solution
        #
        # if none of the numbers lead to a solution, something must have gone
        # wrong previously. return false
        success = False
        for num in range(1,10):
            if self.check(num,i,j):
                self.grid[i][j] = num
                self.rows[i].add(num)
                self.cols[j].add(num)
                self.tiles[tile(i,j)].add(num)
                success = self.solveFrom(*next(i,j))
                if success:
                    return True
                else:
                    self.rows[i].remove(num)
                    self.cols[j].remove(num)
                    self.tiles[tile(i,j)].remove(num)
        if not success:
            self.grid[i][j] = 0
            return False


    # print the sudoku grid
    # TODO: prettify?
    def print_grid(self):
        for i in range(9):
            print(self.grid[i])

    # wrapper function to solve sudoku
    def solve(self):
        if self.solveFrom(0,0):
            print("Success!")
            print("--------------------------")
            print("Solution:")
            self.print_grid()
        else:
            print("This sudoku has no solution!")


grid1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

grid2 =[
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

g = Grid(grid1)

if __name__ == "__main__":
    g.solve()
