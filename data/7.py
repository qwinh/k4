input_file = "6.txt"
output_file = "7.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order (original ones)
replacements = [
    ("=1", "w"),
    ("=2", "i"),
    ("=3", "e"),
    ("=4", "q"),
    ("=5", "o"),
    ("1", "s"),
    ("2", "k"),
    ("3", "d"),
    ("4", "a"),
    ("5", "l"),
    ("QQ", "qz"),
    ("AA", "az"),
    ("WW", "wz"),
    ("SS", "sz"),
    ("EE", "ez"),
    ("DD", "dz"),
    ("II", "iz"),
    ("KK", "kz"),
    ("OO", "oz"),
    ("LL", "lz"),
    ("PP", "pz"),
    ("ZZ", "zz"),
]




# Split the text into words
words = text.split()

# Process each word: check replacements in order, replace the first matching one (leftmost occurrence)
modified_words = []
for word in words:
    replaced = False
    for old, new in replacements:
        pos = word.find(old)
        if pos != -1:
            new_word = word[:pos] + new + word[pos + len(old):]
            modified_words.append(new_word)
            replaced = True
            break
    if not replaced:
        modified_words.append(word)

# Join back into text
text = ' '.join(modified_words)

# Save to a new file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")