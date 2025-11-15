input_file = "1d1.txt"
output_file = "2.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order
replacements = [
    ("gh", "g"),
    ("ng ", "f "),
    ("ch ", "c "),
    ("nh ", "f "),
    ("i ",  "j "),
    ("o ",  "u "),
    ("y ",  "j "),
    ("p ",  "v "),
    ("t ",  "r "),
]

# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
