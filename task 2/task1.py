def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print(result)
# The representation used is octal (base 8), as 'o' specifies octal format in Python's format function.