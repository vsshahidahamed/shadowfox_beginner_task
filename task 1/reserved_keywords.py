import keyword

# Display all reserved keywords in Python
print("Python Reserved Keywords:")
print("=" * 50)
print(keyword.kwlist)
print("\n" + "=" * 50)
print(f"Total reserved keywords: {len(keyword.kwlist)}")

# Show why 'for' is a keyword
print(f"\nIs 'for' a keyword? {keyword.iskeyword('for')}")
print(f"Is 'myvar' a keyword? {keyword.iskeyword('myvar')}")
