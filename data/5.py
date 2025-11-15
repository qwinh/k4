input_file = "4.txt"
output_file = "5.txt"

# Read the file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# All replacements listed in order
replacements = [
    ("k_", "c_"),
    ("q_", "c_"),
    ("gh_", "g_"),
    ("ch_", "u_"),
    ("tr_", "o_"),

    ("th_", "w_"),
    ("đ_",  "j_"),

    ("ng_", "a_"),
    ("nh_", "i_"),

    ("k_",  "c_"),
    ("q_",  "c_"),

    ("gi_", "z_"),
    #("\n_",   "\np_"),
]



# Apply all replacements sequentially
for old, new in replacements:
    text = text.replace(old, new)

# Save
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"All replacements done. Output saved to '{output_file}'")
