def count_alive_neighbors(grid, row, col):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 29 and 0 <= new_col < 29 and grid[new_row][new_col] != '-':
                count += 1
    return count

def play_game(player_char, grid):
    max_color = 'w' if player_char == 'b' else 'b'
    max_count = 0
    max_position = None

    for row in range(29):
        for col in range(29):
            if grid[row][col] == '-':
                alive_neighbors = count_alive_neighbors(grid, row, col)
                grid[row][col] = player_char
               
                if player_char == 'w':
                    player_count = alive_neighbors
                else:
                    player_count = 8 - alive_neighbors
               
                if player_count > max_count:
                    max_count = player_count
                    max_position = (row, col)
               
                grid[row][col] = '-'
   
    return max_position


player_char = input().strip()
grid = [list(input().strip()) for _ in range(29)]


result = play_game(player_char, grid)
if result is not None:
    row, col = result
    print(row, col)
else:
    print('0 0')