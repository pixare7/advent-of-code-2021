# day 3 - Binary diagnostic - Part 1 

from statistics import mode
from collections import Counter

# open the file in read mode
file = open('input.txt', 'r')

rows = []
gamma_rate = ''

ones = 0
zeros = 0

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    row = list(row)
    rows.append(row) 

modes = []

for i in range(len(rows[0])):
    gamma_rate += str(mode([int(j[i]) for j in rows]))

epsilon_rate = ''.join(['1' if i == '0' else '0' for i in list(gamma_rate)])


# takes binary num and turns it into a standard integer
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

power_consumption = gamma_rate*epsilon_rate

print(gamma_rate)
print(epsilon_rate)
print(f"The power consumption is {power_consumption}.")

