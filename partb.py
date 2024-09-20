from parta import Queue

# grid: A 2D list representing the grid of numbers.
# Returns:
#   A list of tuples (row, col) indicating the cells that will overflow.
#   Returns None if no cells will overflow.
def get_overflow_list(grid):
    overflow_list = []
    numRows = len(grid)
    numCols = len(grid[0])

    for row in range(numRows):
        for col in range(numCols):
            neighbours = 0
            if col > 0: # Check left neighbour
                neighbours += 1
            if col < numCols - 1: # Check right neighbour
                neighbours += 1
            if row > 0: # Check upper neighbour
                neighbours += 1
            if row < numRows - 1: # Check lower neighbour
                neighbours += 1
            
            if abs(grid[row][col]) >= neighbours and abs(grid[row][col]) != 0:
                overflow_list.append((row, col))
    
    if not overflow_list:
        return None
    else:
        return overflow_list

# Checks if the grid is in an overflow state by comparing signs of the cells.
# grid: A 2D list representing the grid of numbers.
# Returns:
#   True if the grid contains cells with different signs and has one or more cells in an overflow state.
#   Returns False otherwise.
def check_sign_overflow_status(grid):
    sign = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = grid[row][col]
            temp_sign = 1 if value > 0 else -1 # Determine the sign of the current cell

            if sign is None:
                sign = temp_sign
            else:
                if sign != temp_sign and value != 0:
                    return True # Return True if there is a cell with a different sign
    return False

# Performs the overflow operation on the grid and adds intermediate results to a queue.
# grid: A 2D list representing the grid of numbers.
# a_queue: An instance of the Queue data structure.
# Returns the number of grids added to the queue.
def overflow(grid, a_queue):
    numRows = len(grid)
    numCols = len(grid[0])

    overflow_list = get_overflow_list(grid)

    def perform_overflow():
        # Sets up and performs the overflow operation on the grid.
        sign = 0
        
        for row, col in overflow_list:
            if grid[row][col] > 0:
                sign = 1
            else:
                sign = -1
            grid[row][col] = sign # Mark the cell with the sign of the overflow
        
        new_grid = [row[:] for row in grid]  # Create a copy of the current grid
        for row, col in overflow_list:
            new_grid[row][col] = 0 # Set the overflowing cell to 0
        
        for row, col in overflow_list:
            if col > 0:
                if new_grid[row][col - 1] * grid[row][col] < 0: 
                    new_grid[row][col - 1] *= -1 # Adjust the sign of the left neighbour
                new_grid[row][col - 1] += grid[row][col]
            if col < numCols - 1:
                if new_grid[row][col + 1] * grid[row][col] < 0: 
                    new_grid[row][col + 1] *= -1 # Adjust the sign of the right neighbour
                new_grid[row][col + 1] += grid[row][col]
            if row > 0:
                if new_grid[row - 1][col] * grid[row][col] < 0: 
                    new_grid[row - 1][col] *= -1 # Adjust the sign of the upper neighbour
                new_grid[row - 1][col] += grid[row][col]
            if row < numRows - 1:
                if new_grid[row + 1][col] * grid[row][col] < 0: 
                    new_grid[row + 1][col] *= -1 # Adjust the sign of the lower neighbour
                new_grid[row + 1][col] += grid[row][col]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                grid[row][col] = new_grid[row][col] # Update the original grid with the new values
        return 1

    if overflow_list is not None:
        overflow_status = check_sign_overflow_status(grid)
        if overflow_status:
            count = perform_overflow()
            a_queue.enqueue([row[:] for row in grid])  # Enqueue the updated grid
            return count + overflow(grid, a_queue) # Recursively call overflow
    return 0