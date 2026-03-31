# Task 4: Dictionary and List Operations

# Part 1: Create a list of friends' names and tuples with name lengths
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

name_lengths = [(name, len(name)) for name in friends]

print("List of tuples (name, length):")
print(name_lengths)

# Part 2: Track expenses with dictionaries
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
total_you = sum(your_expenses.values())
total_partner = sum(partner_expenses.values())

print(f"\nYour total expenses: {total_you}")
print(f"Partner's total expenses: {total_partner}")

# Determine who spent more
if total_you > total_partner:
    print("You spent more money overall.")
elif total_partner > total_you:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount.")

# Find the category with the most significant difference
differences = {category: abs(your_expenses.get(category, 0) - partner_expenses.get(category, 0)) for category in set(your_expenses) | set(partner_expenses)}
max_diff_category = max(differences, key=differences.get)
print(f"The category with the most significant difference is '{max_diff_category}' with a difference of {differences[max_diff_category]}")