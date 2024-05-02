import copy
import heapq

class Node:
    def __init__(self, mat, x, y, gscore, parent=None):
        self.mat = mat
        self.x = x
        self.y = y
        self.gscore = gscore
        self.parent = parent
        self.hscore = self.calculate_cost()

    def calculate_cost(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.mat[i][j] != 0 and self.mat[i][j] != final[i][j]:
                    count += 1
        return count

    def __lt__(self, other):
        return (self.hscore + self.gscore) < (other.hscore + other.gscore)

def print_matrix(mat):
    for row in mat:
        print(*row)

def is_safe(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def print_path(root):
    if not root:
        return
    print_path(root.parent)
    print_matrix(root.mat)
    print("hscore:", root.hscore)
    print("gscore:", root.gscore)
    print("fscore:", root.hscore + root.gscore, "\n")

def solve(initial, x, y, final):
    pq = []
    root = Node(initial, x, y, 0)
    heapq.heappush(pq, root)
    while pq:
        min_node = heapq.heappop(pq)
        if min_node.hscore == 0:
            print_path(min_node)
            return
        for i, j in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            if is_safe(min_node.x + i, min_node.y + j):
                new_mat = copy.deepcopy(min_node.mat)
                new_mat[min_node.x][min_node.y], new_mat[min_node.x + i][min_node.y + j] = new_mat[min_node.x + i][min_node.y + j], new_mat[min_node.x][min_node.y]
                child = Node(new_mat, min_node.x + i, min_node.y + j, min_node.gscore + 1, min_node)
                heapq.heappush(pq, child)

initial = [[0]*3 for _ in range(3)]
x, y = 0, 0

print("\nEnter Initial Block Structure\nEnter 0 for blank space:")
for i in range(3):
    for j in range(3):
        initial[i][j] = int(input("Row {} Column {} Element = ".format(i + 1, j + 1)))
        if initial[i][j] == 0:
            x, y = i, j

final = [[0]*3 for _ in range(3)]
print("\nEnter Final Block Structure\nEnter 0 for blank space:")
for i in range(3):
    for j in range(3):
        final[i][j] = int(input("Row {} Column {} Element = ".format(i + 1, j + 1)))

print("\nInitial Structure:")
print_matrix(initial)
print("\nFinal Structure:")
print_matrix(final)
print("\n\nThis is the solution using A* Algorithm:\n")
solve(initial, x, y, final)
