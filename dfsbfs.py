from collections import deque

def main():
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of edges: "))
    a = [[0] * n for _ in range(n)]
    print("Now enter vertex numbers between which edges are present")
    for _ in range(m):
        v1 = int(input("Vertex: "))
        v2 = int(input("Vertex: "))
        print(f"Vertex {v1} <---------> Vertex {v2}")
        a[v1][v2] = 1
        a[v2][v1] = 1
    
    q = deque()
    visited = [False] * n
    
    root_vertex = int(input("Enter the root vertex: "))
    q.append(root_vertex)
    
    print("\nFollowing is the BFS traversal of the provided graph:")
    while q:
        x = q.popleft()
        if not visited[x]:
            print(x, end=" ")
            visited[x] = True
            for i in range(n):
                if a[x][i] == 1 and not visited[i]:
                    q.append(i)
    
    visited = [False] * n
    s = [root_vertex]
    
    print("\n\nFollowing is the DFS traversal of the provided graph:")
    while s:
        x = s.pop()
        if not visited[x]:
            print(x, end=" ")
            visited[x] = True
            for i in range(n-1, -1, -1):
                if a[x][i] == 1 and not visited[i]:
                    s.append(i)

if __name__ == "__main__":
    main()
