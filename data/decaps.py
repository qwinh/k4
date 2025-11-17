# convert all uppercase letters in a large text file to lowercase

input_path = "nam_hoa_kinh.txt"
output_path = "nam_hoa_kinh-decaps.txt"

with open(input_path, "r", encoding="utf-8") as src, \
     open(output_path, "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line.lower())
