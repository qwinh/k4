# apply_whole_file_variations.py
# Reads input.txt and writes output.txt
# Behavior:
#  - write original file content first
#  - then for each mapping (q,w,j,...):
#      produce a full copy of the file where any key that starts with '0'
#      has that leading '0' replaced by the mapping letter and the mapped
#      string prefixed to the value. Append that block to the output.

maps = {
    "b": "q",
}

input_file = "0_q_.txt"
output_file = "0_q_1_.txt"

def make_variations(input_path, output_path, maps_dict, encoding="utf-8"):
    # read original lines (keep original whitespace except strip trailing newline)
    with open(input_path, "r", encoding=encoding) as f:
        lines = [line.rstrip("\n") for line in f]

    with open(output_path, "w", encoding=encoding) as out:
        # for each mapping, append a full-file variation
        for letter, mapped in maps_dict.items():
            # optional: separate blocks with a blank line for readability
            out.write("\n")  

            for line in lines:
                # if the line doesn't contain a tab, copy it as-is
                if "\t" not in line:
                    out.write(line + "\n")
                    continue

                key, val = line.split("\t", 1)

                if key.startswith("0"):
                    new_key = letter + key[1:]
                    new_val = mapped + val
                    out.write(f"{new_key}\t{new_val}\n")
                else:
                    # line's key does not start with '0', copy unchanged
                    out.write(line + "\n")

if __name__ == "__main__":
    make_variations(input_file, output_file, maps)
