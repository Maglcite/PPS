RESET = "\033[0m"
PURPLE = "\033[45m"

def find_valid_paths(grid, target_sum, start_row, start_col, exit_row, exit_col,
                     current_row=None, current_col=None, current_path=[], current_total=0, valid_paths=[]):
    if current_row is None:
        current_row, current_col = start_row, start_col
    if current_row < 0 or current_col < 0 or current_row >= 3 or current_col >= 3 or (current_row, current_col) in current_path:
        return valid_paths
    current_total += grid[current_row][current_col]
    new_path = current_path + [(current_row, current_col)]
    if (current_row, current_col) == (exit_row, exit_col) and current_total == target_sum:
        valid_paths.append(new_path)
        return valid_paths
    find_valid_paths(grid, target_sum, start_row, start_col, exit_row, exit_col, current_row, current_col + 1, new_path, current_total, valid_paths)
    find_valid_paths(grid, target_sum, start_row, start_col, exit_row, exit_col, current_row, current_col - 1, new_path, current_total, valid_paths)
    find_valid_paths(grid, target_sum, start_row, start_col, exit_row, exit_col, current_row + 1, current_col, new_path, current_total, valid_paths)
    return valid_paths

def show_grid(grid, start_row, start_col, exit_row, exit_col, solution_path):
    for row_index in range(3):
        row_display = [
            f"{PURPLE if solution_path and (row_index, col_index) in solution_path else ''}{str(grid[row_index][col_index]).center(5)}{RESET}"
            for col_index in range(3)
        ]
        print(" | ".join(row_display))
        if row_index < 2:
            print("-" * 19)

target_total = int(input("Enter the target total: "))

# Ask for 9 numbers in one line (e.g., "1 2 3 4 5 6 7 8 9")
all_numbers = list(map(int, input("Enter the 9 numbers): ").split()))
grid = [all_numbers[i * 3:(i + 1) * 3] for i in range(3)]

start_row, start_col = map(int, input("Enter the start in row+column format pretty please): ").split())
exit_row, exit_col = map(int, input("Enter the exit pos in the same format pretty please): ").split())

valid_paths = find_valid_paths(grid, target_total, start_row, start_col, exit_row, exit_col)
solution_path = valid_paths[0] if valid_paths else []
show_grid(grid, start_row, start_col, exit_row, exit_col, solution_path)
