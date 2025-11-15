import unicodedata

def remove_tone_and_get_symbol(char):
    """
    Convert a single Vietnamese Unicode character to its tone-removed equivalent
    and return the tone symbol if present. Handles both lowercase and uppercase.
    Non-Vietnamese characters are returned as-is.
    """
    decomp = unicodedata.normalize('NFD', char)
    parts = list(decomp)
    if len(parts) == 1:
        return char, None

    base = parts[0]
    diacs = []  # combining diacritics except tones
    tone_mark = None

    for p in parts[1:]:
        code = ord(p)
        if code in [0x0301, 0x0300, 0x0309, 0x0303, 0x0323]:  # tone marks
            if tone_mark is not None:
                # Assume only one tone per character; keep the first if multiple
                pass
            if code == 0x0301:  # acute
                tone_mark = "1"
            elif code == 0x0300:  # grave
                tone_mark = "2"
            elif code == 0x0309:  # hook above
                tone_mark = "3"
            elif code == 0x0303:  # tilde
                tone_mark = "4"
            elif code == 0x0323:  # dot below
                tone_mark = "5"
        else:
            # Other diacritics (circumflex, breve, horn, etc.)
            diacs.append(p)

    # Reconstruct neutral form: base + diacritics (no tone)
    neutral_decomp = base + ''.join(diacs)
    neutral = unicodedata.normalize('NFC', neutral_decomp)
    return neutral, tone_mark

def process_syllable(syllable):
    """
    Process a single syllable (word) to remove tones and append the tone symbol
    at the end if present. Assumes one tone per syllable.
    """
    neutrals = []
    tone = None
    for c in syllable:
        neu, t = remove_tone_and_get_symbol(c)
        neutrals.append(neu)
        if t:
            tone = t  # Assume only one tone per syllable
    neutral_word = ''.join(neutrals)
    if tone:
        return neutral_word + tone
    else:
        return neutral_word

def viet_to_tone_sep(text):
    """
    Convert a full Vietnamese text string to tone-separated form.
    Splits on spaces, processes each syllable, and rejoins.
    """
    words = text.split()
    processed = [process_syllable(w) for w in words]
    return ' '.join(processed)

# File I/O script
if __name__ == "__main__":
    input_prefix = 'truyen-kieu_one-line'
    input_file = input_prefix + '.txt'  # Adjust to your input file path
    output_file = input_prefix + '_tone_sep.txt'  # Output file path
    
    with open(input_file, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    
    tone_sep_content = viet_to_tone_sep(content)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(tone_sep_content)
    
    print(f"Conversion complete. Output saved to {output_file}")