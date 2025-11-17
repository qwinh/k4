import sys

def main():
    input_path = "mul.txt"
    output_path = "muled.txt"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        with open(output_path, 'w', encoding='utf-8') as out:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 2:
                    continue  # Skip invalid lines
                word = parts[0]
                try:
                    count = int(parts[1])
                except ValueError:
                    continue  # Skip if count is not integer
                repeated = ' '.join([word] * count)
                out.write(repeated + '\n')
    
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()