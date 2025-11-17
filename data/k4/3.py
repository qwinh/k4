def process_words(input_string):
    words = input_string.split()
    processed_words = []
    
    for word in words:
        if word and word[-1].isdigit():
            num = word[-1]
            base = word[:-1]
            # Find the position right after the rightmost uppercase letter
            insert_pos = -1
            for i in range(len(base) - 1, -1, -1):
                if base[i].isupper():
                    insert_pos = i + 1
                    break
            if insert_pos != -1:
                result = base[:insert_pos] + num + base[insert_pos:]
            else:
                result = base + num
            processed_words.append(result)
        else:
            processed_words.append(word)
    
    return ' '.join(processed_words)

input_file = "1.txt"
output_file = "1d1.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

processed = process_words(content)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(processed)

print("Processing complete. Output written to", output_file)