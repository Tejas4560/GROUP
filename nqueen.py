def is_valid(grid, row, col):
    for i in range(col):
        if grid[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if grid[i][j] == 1:
            return False
    for i, j in zip(range(row, len(grid), 1), range(col, -1, -1)):
        if grid[i][j] == 1:
            return False
    return True

def place_queens(grid, col):
    if col >= len(grid):
        return True
    for i in range(len(grid)):
        if is_valid(grid, i, col):
            grid[i][col] = 1
            if place_queens(grid, col + 1):
                return True
            grid[i][col] = 0
    return False

def display(grid):
    for row in grid:
        for cell in row:
            if cell:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    grid = [[0] * n for _ in range(n)]
    if place_queens(grid, 0):
        display(grid)
    else:
        print("No solution exists.")
