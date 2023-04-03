# Initialize a random grid (size*size) of range between 3 and 7 via random library
import random
grid = []
list_of_symbol = ["#", "-"]
size = random.randrange(3, 7)
for _ in range(size):
    inside_list = [random.choice(list_of_symbol) for _ in range(size)]
    grid.append(inside_list)


def minesweeper(grid):

    # Helper 1: address index-out-of-range issues by setting up valid positions
    def valid_position(grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    # Helper 2: count surrounding mines for each '-'
    def count_adjacent_mines(grid, row, col):
        positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for row_position, col_position in positions:
            new_row, new_col = row + row_position, col + col_position
            if valid_position(grid, new_row, new_col) and grid[new_row][new_col] == '#':
                count += 1
        return count

    # Initialize a new grid
    new_grid = []

    # Use of enumerate() where we search for rows in the initial grid
    for index_row, symbol_row in enumerate(grid):
        # Initialize the nested list
        inner_row = []
        # Find the element located within the row of the initial grid
        for index_col, symbol in enumerate(symbol_row):
            # Replace '-' by the corresponding count, otherwise '#'
            new_item = count_adjacent_mines(grid, index_row, index_col) if symbol == '-' else symbol
            # Append to the nested list
            inner_row.append(new_item)
        # Append to the list
        new_grid.append(inner_row)
    return new_grid

# Propose to display the input as matrix
print('Example of input: ')
initial = grid
for row in grid:
    print(row)

# Output after calling the function minesweeper(grid); display as matrix
print('Output: ')
result = minesweeper(grid)
for row in result:
    print(row)




