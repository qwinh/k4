input_file = "5.txt"
output_file = "6.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order (original ones)
replacements = [
    ("QQ-", "Q="),
    ("AA-", "A="),
    ("WW-", "W="),
    ("SS-", "S="),
    ("EE-", "E="),
    ("DD-", "D="),
    ("II-", "I="),
    ("KK-", "K="),
    ("OO-", "O="),
    ("LL-", "L="),
    ("PP-", "P="),
    ("ZZ-", "Z="),
]


# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
