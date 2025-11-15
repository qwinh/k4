input_file = "4.txt"
output_file = "5.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order (original ones)
replacements = [
    ("1", "-1"),
    ("2", "-2"),
    ("3", "-3"),
    ("4", "-4"),
    ("5", "-5"),
]


# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
