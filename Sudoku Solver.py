from random import shuffle

# Inspired by https://www.101computing.net/sudoku-generator-algorithm/
# This project was inspired by another project. As I tried to solve this program I had to take inspiration on certain
# features. None of this code was copy pasted. I tried to solve this project as much on my own as possible.


# Step 1: Create an empty sudoku nested list with 0 instead of blanks. For each row of 9 create a list. Optionally
# add instead of 0 in sud_grid your own numbers from an existing unfilled sudoku and let the program finish it for
# you...
sud_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Step 2: Create a list of all possible numbers in nested list.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 3: Print out Empty/not finished grid in terminal using a for loop to print every "line" element on single line.
for line in sud_grid:
    print(line)


# Step 4: Make a function to check if grid is full and with no zeroes. If any 0 in grid function prints false. If all ok
# function prints True.
def checksud(sud_grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if sud_grid[row][col] == 0:
                return False
    return True


print(checksud(sud_grid))


# Step 5: Make a function to fill in all the zero digits.
def fillgrid(sud_grid):
    # Step 5.1: Make a for loop to generate all the possible coordinates for rows and cols.
    for i in range(0, 81):  # "i" will loop in the range from 0 to 81 (not including 81.) "i" will go 01234....79,80.
        row = i // 9  # to generate the row coordinates for each element we use //. Which means each "i" is divided by 9
        # and make a floor number. Thus 1//9 = 0, 11//9 = 1.....
        col = i % 9  # to make column coordinate will use % symbol which leaves us the remainder of each division.
        # Thus 1 % 9 = 1, 12 % 9 = 3....
        if sud_grid[row][col] == 0:  # function will go through all possible coordinates and if it == 0 will go further.
            shuffle(num_list)  # makes a random shuffle of given list 123....
            for value in num_list:  # makes a for loop for every value in shuffled num_list
                if not (value in sud_grid[row]):  # if given value is not in given row program will proceed further.
                    # To check if value is not in column use all row values and keep current column value.
                    if not (value in (
                            sud_grid[0][col], sud_grid[1][col], sud_grid[2][col], sud_grid[3][col], sud_grid[4][col],
                            sud_grid[5][col], sud_grid[6][col], sud_grid[7][col], sud_grid[8][col])):
                        # Identify which of the 9 squares we are working on
                        if row < 3:
                            if col < 3:
                                square = [sud_grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [sud_grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [sud_grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [sud_grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [sud_grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [sud_grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [sud_grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [sud_grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [sud_grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not (value in (square[0] + square[1] + square[2])):
                            sud_grid[row][col] = value
                            if checksud(sud_grid):
                                return True
                            else:
                                if fillgrid(sud_grid):
                                    return True
            break
    sud_grid[row][col] = 0


# Generate a Fully Solved Grid
fillgrid(sud_grid)

for fullsud in sud_grid:
    print(fullsud)

print(checksud(sud_grid))
