file_path = './inputs/Day6.txt'
wall = '#'
guard = '^'
visited = set()

def file_to_2d_array(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    array_2d = [list(line.strip()) for line in lines]
    return array_2d

def move(grid, x, y, direction):
    if direction == "up":
        while x > 0 and grid[x-1][y] != wall:
            x -= 1
            visited.add((x, y))
        if x > 0 and grid[x-1][y] == wall:
            direction = "right"
    elif direction == "right":
        while y < len(grid[0]) - 1 and grid[x][y + 1] != wall:
            y += 1
            visited.add((x, y))
        if y < len(grid[0]) - 1 and grid[x][y + 1] == wall:
            direction = "down"
    elif direction == "down":
        while x < len(grid) - 1 and grid[x + 1][y] != wall:
            x += 1
            visited.add((x, y))
        if x < len(grid) - 1 and grid[x + 1][y] == wall:
            direction = "left"
    elif direction == "left":
        while y > 0 and grid[x][y - 1] != wall:
            y -= 1
            visited.add((x, y))
        if y > 0 and grid[x][y - 1] == wall:
            direction = "up"
    return x, y, direction

def find_start(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == guard:
                return i, j
    return None

grid = file_to_2d_array(file_path)

start_x, start_y = find_start(grid)
visited.add((start_x, start_y))
direction = "up"

while True:
    previous_position = (start_x, start_y)
    start_x, start_y, direction = move(grid, start_x, start_y, direction)

    if (start_x, start_y) == previous_position:
        break

print("Number of unique coordinates visited:", len(visited))
