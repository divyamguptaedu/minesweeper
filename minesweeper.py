""" 
    The Minesweeper Game 
    Author: Divyam Gupta
"""

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

def show_gameboard(layout):
	rows_count = layout["rows"]
	cols_count = layout["cols"]

	alpha = "abcdefghijklmnopqrstuvwxyz"
	column_label = "		  "
	for position in range(0, cols_count):
		column_label = column_label + alpha[position].upper() + "    "

	horizontal_line = "		" + (5 * cols_count * '-')

	for i in range(4):
		print ""	

	print column_label
	print horizontal_line

	for row in range(1, rows_count + 1):
		row_layout = '{0:14} |'.format(row)
		for i in range(0, rows_count):
			row_layout = row_layout + "    |"
		
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

	show_gameboard(gameboard_layout)
	
	in_memory_grid = [[" " for j in range(gameboard_layout["cols"])] for i in range(gameboard_layout["rows"])]

	return (in_memory_grid, gameboard_layout["mines"])

def if_valid_input(in_memory_grid, input):
	input_length = len(input)

	row = -1
	col = -1
	flag = ""

	alpha = "abcdefghijklmnopqrstuvwxyz"
	board_dimensions = {"rows": range(1, (len(in_memory_grid) + 1)), "cols": alpha[0:len(in_memory_grid[0])].upper()}

	if input_length == 2:
		row = int(input[0])
		col = input[1].upper()
		
		if row in board_dimensions["rows"] and col in board_dimensions["cols"]:
			return (row, col)

	if input_length == 3 and input[2].upper() == "F":
		row = int(input[0])
		col = input[1].upper()
		flag = input[2].upper()

		if row in board_dimensions["rows"] and col in board_dimensions["cols"]:
			row_index, col_index = (row - 1, alpha.upper().index(col))

			#TODO
			if in_memory_grid[row_index][col_index] == " ":
				in_memory_grid[row_index][col_index] = "F"
			elif in_memory_grid[row_index][col_index] == "F":
				in_memory_grid[row_index][col_index] = " "

			return (row, col)

	else:
		return -1

"""def make_grid(in_memory_grid, mines, first_cell):
	grid = [["0" for j in range(len(in_memory_grid))] for i in range(len(in_memory_grid))]"""


def main():

	flag_cord = []
	mine_cord = []
	display_grid = []

	welcome()
	player_info = show_menu()
	(in_memory_grid, mines) = create_gameboard(player_info)
	
	while True:
		user_input = raw_input("Type ROW index followed by the COLUMN label : ")
		first_cell = if_valid_input(in_memory_grid, str(user_input))
		"""if first_cell != -1:
			if display_grid == []:
				display_grid = make_grid(in_memory_grid, mines, first_cell)"""
		print first_cell

	



main()
