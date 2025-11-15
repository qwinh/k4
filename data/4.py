input_file = "3.txt"
output_file = "4.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order
replacements = [
    ("1", "-s"),
    ("2", "-k"),
    ("3", "-d"),
    ("4", "-a"),
    ("5", "-l"),
]


# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
