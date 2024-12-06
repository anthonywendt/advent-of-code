# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# parse the map and locate the starting position and direction
def parse_map(input_data):
    grid = [list(line) for line in input_data.strip().splitlines()]
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] in "^>v<":
                start_pos = (x, y)
                start_dir = "^>v<".index(grid[x][y])  # Map direction to index
                grid[x][y] = "."  # Clear the starting position
                return grid, start_pos, start_dir

    raise ValueError("Starting position not found in the map.")

# move around the map and count the number of distinct positions visited. Will bail out if a loop is detected
def move_around_map(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    x, y = start_pos
    direction = start_dir

    visited_distinct_positions = set()  # Store all distinct positions
    visited_distinct_positions.add((x, y))  # Add starting position
    visited_state = set()  # Store all positions with direction for loop check
    start = True

    while 0 <= x < rows and 0 <= y < cols:
        current_state = (x, y, direction)
        if not start and current_state in visited_state:
            return True, 0 # Loop detected
        visited_state.add(current_state)
        start = False

        # Move in the current direction
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if not (0 <= nx < rows and 0 <= ny < cols):
            break

        # Check if the next position is a wall
        if grid[nx][ny] == "#":
            # Rotate right by 90 degrees
            direction = (direction + 1) % 4
        else:
            # Move to the next position
            x, y = nx, ny
            visited_distinct_positions.add((x, y))  # Add new position to the set

    return False, len(visited_distinct_positions)

# brute force all possible positions where a # can be placed and create a trap
def count_possible_trapping_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    trapping_positions = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == ".":
                # Temporarily place a # and test for a loop
                grid[x][y] = "#"
                loop_detected, _ = move_around_map(grid, start_pos, start_dir)
                if loop_detected:
                    trapping_positions += 1
                grid[x][y] = "."  # Remove the # after testing

    return trapping_positions

if __name__ == '__main__':

    grid, start_pos, start_dir = parse_map(read_input('input.txt'))

    print(f"puzzle 1 result: {move_around_map(grid, start_pos, start_dir)}")
    print(f"puzzle 2 result: {count_possible_trapping_positions(grid, start_pos, start_dir)}")
