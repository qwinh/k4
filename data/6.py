input_file = "5.txt"
output_file = "6.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order
replacements = [
    ("ng-", "f-"),
    ("ch-", "c-"),
    ("nh-", "f-"),
    ("i-",  "j-"),
    ("o-",  "u-"),
    ("y-",  "j-"),
    ("p-",  "v-"),
    ("t-",  "r-"),
    ("_QQ", "_q"),
    ("_AA", "_a"),
    ("_WW", "_w"),
    ("_SS", "_s"),
    ("_EE", "_e"),
    ("_DD", "_d"),
    ("_II", "_i"),
    ("_KK", "_k"),
    ("_OO", "_o"),
    ("_LL", "_l"),
    ("_PP", "_p"),
    ("_ZZ", "_z"),
]




# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
