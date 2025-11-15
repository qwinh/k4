import re

input_file = "3.txt"
output_file = "4.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order (original ones)
replacements = [
    (" Q", "pQ"),
    (" A", "pA"),
    (" W", "pW"),
    (" S", "pS"),
    (" E", "pE"),
    (" D", "pD"),
    (" I", "pI"),
    (" K", "pK"),
    (" O", "pO"),
    (" L", "pL"),
    (" P", "pP"),
    (" Z", "pZ"),
]

# Perform replacements on the entire text with constraint
for old, new in replacements:
    letter = old[1]
    pattern = r' ' + re.escape(letter) + r'(\d)? '
    replacement = r' p' + letter + r'\1 '
    text = re.sub(pattern, replacement, text)

# Save to a new file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")