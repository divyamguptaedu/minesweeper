from random import randint


def welcome():
	""" Created using http://patorjk.com/software/taag/ """
	print("  __  __ _                                                   ")
	print(" |  \/  (_)                                                  ")
	print(" | \  / |_ _ __   ___  _____      _____  ___ _ __   ___ _ __ ")
	print(" | |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|")
	print(" | |  | | | | | |  __/\__ \\\ V  V /  __/  __/ |_) |  __/ |   ")
	print(" |_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   ")
	print("                                            | |              ")
	print("                                            |_|              ")

def show_game_over_message():
	print "Game Over!"

def show_menu():
	player_info = {}
	player_info["name"] = raw_input("Please enter your name: ")
	print("")
	print("Hello " + player_info["name"] + "! Now, on the scale of 1 to 3, ")
	player_info["difficulty_level"] = raw_input("Please choose the difficulty level: ")
	print("")
	print("Type the ROW number followed by the COLUMN and press ENTER to explore.")
	print("Add F to desired cell's coordinates to add/remove flag.")

	return player_info


def show_gameboard(grid):
	rows_count = len(grid)
	cols_count = len(grid[0])

	alpha = "abcdefghijklmnopqrstuvwxyz"
	column_label = "		  "
	for position in range(0, cols_count):
		column_label = column_label + alpha[position].upper() + "    "

	horizontal_line = "		" + (5 * cols_count * '-')

	for i in range(4):
		print ""	

	print column_label
	print horizontal_line

	for row in range(0, rows_count):
		row_layout = '{0:14} |'.format(row + 1)
		for i in grid[row]:
			row_layout = row_layout + "  " + str(i) + " |"
		
		print row_layout
		print horizontal_line

	for i in range(4):
		print ""

def create_gameboard(player_info):
	difficulty_level = int(player_info["difficulty_level"])
	gameboard_layout = {}

	if difficulty_level == 1:
		gameboard_layout["rows"] = 10
		gameboard_layout["cols"] = 10
		gameboard_layout["mines"] = 10

	if difficulty_level == 2:
		gameboard_layout["rows"] = 15
		gameboard_layout["cols"] = 15
		gameboard_layout["mines"] = 20

	if difficulty_level == 3:
		gameboard_layout["rows"] = 20
		gameboard_layout["cols"] = 20
		gameboard_layout["mines"] = 40

	in_memory_grid = [[" " for j in range(gameboard_layout["cols"])] for i in range(gameboard_layout["rows"])]

	show_gameboard(in_memory_grid)
	
	return (in_memory_grid, gameboard_layout["mines"])

def if_valid_row(in_memory_grid, user_input_row):
	board_dimensions = {"rows": str(range(1, (len(in_memory_grid) + 1)))}
	print board_dimensions
	if (user_input_row) in board_dimensions["rows"]:
		return True
	else:
		return False

def if_valid_col(in_memory_grid, user_input_col):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	board_dimensions = {"cols": alpha[0:len(in_memory_grid[0])].upper()}
	if str(user_input_col).upper() in board_dimensions["cols"]:
		return True
	else:
		return False

def get_user_input_validate(in_memory_grid):
	""" Row """
	user_input_row = raw_input("Type ROW index : ")
	is_row_valid = if_valid_row(in_memory_grid, str(user_input_row))
	while (not is_row_valid):
		print("Please type a valid row number.")
		user_input_row = raw_input("Type ROW index : ")
		is_row_valid = if_valid_row(in_memory_grid, str(user_input_row))

	""" Column """
	user_input_col = raw_input("Type COLUMN index : ")
	is_col_valid = if_valid_col(in_memory_grid, str(user_input_col))
	while (not is_col_valid):
		print("Please type a valid column label.")
		user_input_col = raw_input("Type COLUMN index : ")
		is_col_valid = if_valid_col(in_memory_grid, str(user_input_col))
	alpha = "abcdefghijklmnopqrstuvwxyz"
	user_input_col_index = alpha.index(user_input_col.lower())

	""" Flag """
	user_input_flag = raw_input("Do you want to place FLAG at (" + str(user_input_row) + ", " + str(user_input_col).upper() + ")? (y/n) : ")
	if(user_input_flag.upper()) == "Y":
		flag = True
	else:
		flag = False

	return {"input_row": (int(user_input_row) - 1), "input_col": int(user_input_col_index), "flag": flag}

def get_random_position(grid):
	number_of_rows = len(grid)
	number_of_cols = len(grid[0])

	row = randint(0, number_of_rows - 1)
	col = randint(0, number_of_cols - 1)

	return (row, col)



def insert_mines(grid, number_of_mines, input_cell_info):
	mines_cord = []
	input_cell = (input_cell_info["input_row"], input_cell_info["input_col"])

	for i in range(number_of_mines):
		random_cell = get_random_position(grid)

		while (random_cell == input_cell) or (random_cell in mines_cord):
			random_cell = get_random_position(grid)
		
		mines_cord.append(random_cell)

	for row, col in mines_cord:
		grid[row][col] = 9

	return {"grid": grid, "mines_cord": mines_cord}


def calculate_value(grid, row, col):
	neighbors_values = []

	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if i == 0 and j == 0:
				continue
			elif -1 < (row + i) < len(grid) and -1 < (col + j) < len(grid[0]):
				neighbors_values.append(grid[row + i][col + j])

	return int(neighbors_values.count(9))


def insert_numbers(grid):
	number_of_rows = len(grid)
	number_of_cols = len(grid[0])

	for row in range(number_of_rows):
		for col in range(number_of_cols):
			cell = grid[row][col]
			if cell != 9:
				grid[row][col] = calculate_value(grid, row, col)

	return grid


def create_minesweeper_grid(in_memory_grid, number_of_mines, input_cell_info):
	grid_dimension = {"row": len(in_memory_grid), "col": len(in_memory_grid[0])}
	
	new_grid = [[0 for j in range(grid_dimension["col"])] for i in range(grid_dimension["row"])]
	
	new_grid_with_mines_info = insert_mines(new_grid, number_of_mines, input_cell_info)
	new_grid_with_mines = new_grid_with_mines_info["grid"]
	mines_cord = new_grid_with_mines_info["mines_cord"]
	
	new_grid_with_mines_and_numbers = insert_numbers(new_grid_with_mines)
	
	return {"grid": new_grid_with_mines_and_numbers, "mines_cord": mines_cord}


def handle_flag(in_memory_grid, input_cell_info, flags_cord):
	if input_cell_info["flag"]:
		row = input_cell_info["input_row"]
		col = input_cell_info["input_col"]

		if in_memory_grid[row][col] == " ":
			in_memory_grid[row][col] = "F"
			flags_cord.append((row, col))
		elif in_memory_grid[row][col] == "F":
			in_memory_grid[row][col] = " "
			flags_cord.remove((row, col))

	elif (input_cell_info["input_row"], input_cell_info["input_col"]) in flags_cord:
		print "There is a flag there!"
	
	else:
		return

def explosion(solution_grid, input_cell_info, flags_cord):
	row = input_cell_info["input_row"]
	col = input_cell_info["input_col"]
	
	if solution_grid[row][col] == 9 and (row, col) not in flags_cord:
		return True
	else:
		return False

def showcells(grid, currgrid, rowno, colno):
    # Exit function if the cell was already shown
    if currgrid[rowno][colno] != ' ':
        return

    # Show current cell
    currgrid[rowno][colno] = grid[rowno][colno]

    # Get the neighbors if the cell is empty
    if grid[rowno][colno] == '0':
        for r, c in getneighbors(grid, rowno, colno):
            # Repeat function for each neighbor that doesn't have a flag
            if currgrid[r][c] != 'F':
                showcells(grid, currgrid, r, c)


def explore(in_memory_grid, solution_grid, input_cell_info, flags_cord):
	row = input_cell_info["input_row"]
	col = input_cell_info["input_col"]

	if in_memory_grid[row][col] == " ":
		in_memory_grid[row][col] = solution_grid[row][col]

		if solution_grid[row][col] == 0:
			neighbors = []

			for i in [-1, 0, 1]:
				for j in [-1, 0, 1]:
					if i == 0 and j == 0:
						continue
					elif -1 < (row + i) < len(solution_grid) and -1 < (col + j) < len(solution_grid[0]):
						neighbors.append((row + i, col + j))

			for neighbor in neighbors:
				neighbor_row = neighbor[0]
				neighbor_col = neighbor[1]
				neighbor_cell_info = {"input_row": neighbor_row, "input_col": neighbor_col}
				
				if solution_grid[neighbor_row][neighbor_col] != 9:
					explore(in_memory_grid, solution_grid, neighbor_cell_info, flags_cord)
	else:
		return



def main():

	flags_cord = []
	mines_cord = []
	solution_grid = []

	welcome()
	player_info = show_menu()
	(in_memory_grid, number_of_mines) = create_gameboard(player_info)
	
	while True:
		input_cell_info = get_user_input_validate(in_memory_grid)
		if solution_grid == []:
			grid_info = create_minesweeper_grid(in_memory_grid, number_of_mines, input_cell_info)
			mines_cord = grid_info["mines_cord"]
			solution_grid = grid_info["grid"]

		handle_flag(in_memory_grid, input_cell_info, flags_cord)
		
		if explosion(solution_grid, input_cell_info, flags_cord):
			show_game_over_message()
			return

		explore(in_memory_grid, solution_grid, input_cell_info, flags_cord)




		



			
		for i in solution_grid:
			print i
		show_gameboard(in_memory_grid)


main()
































