# Dive! 

# part 1

# opens the file in read mode
file = open('input.txt', 'r')

horizontal = 0
depth = 0
sub_path = []

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    split_row = tuple(row.split(" ")) # split by space & add to tuple
    split_row = (split_row[0], int(split_row[1])) # convert 2nd item to integer
    sub_path.append(split_row) # add tuple to list

for step in sub_path:
    if step[0] == 'forward':
        horizontal += step[1]
    elif step[0] == 'down':
        depth += step[1]
    else:
        depth -= step[1]

hd = horizontal*depth

print(f"The product of depth and horizontal units is {hd}.")

# ------------------------------------------------------------------------------

# part 2

# opens the file in read mode
file = open('input.txt', 'r')

horizontal = 0
depth = 0
aim = 0
sub_path = []

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    split_row = tuple(row.split(" ")) # split by space & add to tuple
    split_row = (split_row[0], int(split_row[1])) # convert 2nd item to integer
    sub_path.append(split_row) # add tuple to list

for step in sub_path:
    if step[0] == 'forward':
        horizontal += step[1]
        depth += aim*step[1]
    elif step[0] == 'down':
        aim += step[1]
    else:
        aim -= step[1]

hd = horizontal*depth

print(f"The product of depth and horizontal units is {hd}.")
