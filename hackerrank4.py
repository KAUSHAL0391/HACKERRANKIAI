import heapq

def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def a_star_search(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    parents = {}
    g_scores = {start: 0}
    f_scores = {start: manhattan_distance(start, end)}
    open_list = [(f_scores[start], start)]

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == end:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path
        
        visited.add(current)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != '%':
                tentative_g_score = g_scores[current] + 1
                if neighbor not in visited or tentative_g_score < g_scores.get(neighbor, float('inf')):
                    parents[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + manhattan_distance(neighbor, end)
                    heapq.heappush(open_list, (f_scores[neighbor], neighbor))

def main():
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    rows, cols = map(int, input().split())
    grid = [list(input()) for _ in range(rows)]
    
    path = a_star_search(grid, start, end)
    
    print(len(path) - 1)
    for node in path:
        print(node[0], node[1])

if __name__ == "__main__":
    main()
