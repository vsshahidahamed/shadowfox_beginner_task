import random

# Simulate rolling a six-sided die multiple times
rolls = 100  # At least 20, using 100 for better statistics
count_6 = 0
count_1 = 0
count_consec_6 = 0
prev_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    if roll == 6:
        count_6 += 1
        if prev_roll == 6:
            count_consec_6 += 1
    if roll == 1:
        count_1 += 1
    prev_roll = roll

print(f"Total rolls: {rolls}")
print(f"How many times you rolled a 6: {count_6}")
print(f"How many times you rolled a 1: {count_1}")
print(f"How many times you rolled two 6s in a row: {count_consec_6}")