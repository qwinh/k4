input_file = "0d1.txt"
output_file = "1.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order (original ones)
replacements = [
    #qua
    ("quô", "qLL"),
    ("oau", "QQu"),
    ("oay", "QQj"),
    ("au", "Qu"),
    ("ay", "Qj"),

    ("oanh", "SS"),
    ("oach", "QQ"),
    ("uyê", "KK"),
    ("uya", "KK"),
    ("oă", "QQ"),
    ("uâ", "SS"),
    ("uơ", "WW"),
    ("uê", "DD"),
    ("oô", "LL"),
    ("uô", "PP"),
    ("ưa", "ZZ"),
    ("ươ", "ZZ"),
    ("ua", "PP"),
    ("uy", "II"),
    ("oe", "EE"),
    ("oa", "AA"),
    ("oo", "OO"),


    ("anh", "S"),
    ("ach", "Q"),
    ("yê", "K"),
    ("iê", "K"),
    ("ă", "Q"),
    ("â", "S"),
    ("ơ", "W"),
    ("ê", "D"),
    ("e", "E"),
    ("ô", "L"),
    ("ư", "Z"),
    ("gya", "giK"),
    ("gia", "giA"),
    ("gi", "giI"),
    ("ia", "K"),
    ("a", "A"),
    ("o", "O"),
    ("u", "P"),
    ("i", "I"),

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