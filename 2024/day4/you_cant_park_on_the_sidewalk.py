# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# solve puzzle 1 by counting the number of times 'XMAS' appears in the grid
def count_xmas(grid):
    def was_found(x, y, dx, dy):
        """Search for 'XMAS' starting from (x, y) in direction (dx, dy)."""
        for i in range(4):  # 'XMAS' has 4 letters
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != target[i]:
                return 0
        return 1

    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]
    count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                count += was_found(x, y, dx, dy)

    return count

# solve puzzle 2 by counting the number of times 'MAS' X shapes appear in the grid
def count_x_mas_shapes(grid):
    def is_x_shape(x, y):
        """Check if the cell (x, y) forms an X-shaped 'MAS' in any variation."""
        if grid[x][y] != 'A':  # Center must be 'A'
            return 0

        # Define patterns as relative positions of (top-left, bottom-right, top-right, bottom-left)
        patterns = [
            [('M', 'S'), ('M', 'S')],  # Pattern 1: MS / A / MS
            [('S', 'M'), ('S', 'M')],  # Pattern 2: SM / A / SM
            [('M', 'S'), ('S', 'M')],  # Pattern 3: MS / A / SM
            [('S', 'M'), ('M', 'S')]   # Pattern 4: SM / A / MS
        ]

        # count = 0

        for (tl_br, tr_bl) in patterns:
            # Unpack the letters for top-left/bottom-right and top-right/bottom-left
            (tl, br), (tr, bl) = tl_br, tr_bl

            # Check boundary conditions and matching pattern
            if (x - 1 >= 0 and y - 1 >= 0 and grid[x - 1][y - 1] == tl and  # Top-left
                x + 1 < rows and y + 1 < cols and grid[x + 1][y + 1] == br and  # Bottom-right
                x - 1 >= 0 and y + 1 < cols and grid[x - 1][y + 1] == tr and  # Top-right
                x + 1 < rows and y - 1 >= 0 and grid[x + 1][y - 1] == bl):  # Bottom-left
                return 1
        return 0

    rows, cols = len(grid), len(grid[0])
    total_count = 0

    for x in range(rows):
        for y in range(cols):
            total_count += is_x_shape(x, y)

    return total_count

if __name__ == '__main__':

    data = read_input('input.txt')
    data = [list(row) for row in data]

    print(f"XMAS appears this many times: {count_xmas(data)}")
    print(f"X-MAS shapes appear this many times: {count_x_mas_shapes(data)}")
