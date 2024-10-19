# opens the file in read mode
file = open('input.txt', 'r')

# initialize list to add info from .txt file
rows = [] 

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    rows.append(int(row)) # convert from string to integer

# initialize var to count depths which increase
count_depths = 0

# loop through list except last element
for i in range(len(rows) - 1):

    # check if the next element is greater than the current & add to count if so
    if rows[i + 1] > rows[i]:
        count_depths+=1

print(f"The depth increases {count_depths} times.")

# solution was 1581