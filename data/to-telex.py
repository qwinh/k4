import unicodedata

def to_telex(char):
    """
    Convert a single Vietnamese Unicode character to its Telex equivalent.
    Handles both lowercase and uppercase.
    Non-Vietnamese characters are returned as-is.
    """
    is_upper = char.isupper()
    char_lower = char.lower()
    if char_lower == 'đ':
        return 'Dd' if is_upper else 'dd'
    decomp = unicodedata.normalize('NFD', char_lower)
    parts = list(decomp)
    if len(parts) == 1:
        result = parts[0]
    else:
        base = parts[0]
        diac = ''
        tone = ''
        for p in parts[1:]:
            code = ord(p)
            if code == 0x0302:  # circumflex
                if base == 'a':
                    diac = 'a'
                elif base == 'e':
                    diac = 'e'
                elif base == 'o':
                    diac = 'o'
            elif code == 0x0306:  # breve
                diac = 'w'
            elif code == 0x031B:  # horn
                diac = 'w'
            elif code == 0x0301:  # acute
                tone = 's'
            elif code == 0x0300:  # grave
                tone = 'f'
            elif code == 0x0309:  # hook above
                tone = 'r'
            elif code == 0x0303:  # tilde
                tone = 'x'
            elif code == 0x0323:  # dot below
                tone = 'j'
        result = base + diac + tone
    if is_upper and result:
        result = result[0].upper() + result[1:]
    return result

def viet_to_telex(text):
    """
    Convert a full Vietnamese text string to its Telex equivalent.
    """
    return ''.join(to_telex(c) for c in text)

# File I/O script
if __name__ == "__main__":
    input_prefix = 'truyen-kieu_one-line'
    input_file = input_prefix + '.txt'  # Adjust to your input file path
    output_file = input_prefix + '_telex.txt'  # Output file path
    
    with open(input_file, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    
    telex_content = viet_to_telex(content)

    #telex_content = telex_content.replace("uwo", "uo")
    #telex_content = telex_content.replace("uw", "w")
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(telex_content)
    
    print(f"Conversion complete. Output saved to {output_file}")