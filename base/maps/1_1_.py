import unicodedata
# ---------------------------------------------------------
# Tone utilities (your provided logic, adapted for re-toning)
# ---------------------------------------------------------
TONE_CODEPOINTS = {
    0x0301: "acute", # 1
    0x0300: "grave", # 2
    0x0309: "hook", # 3
    0x0303: "tilde", # 4
    0x0323: "dot", # 5
}
def strip_tone(char):
    """
    Remove tone marks from a single Vietnamese character while keeping
    other diacritics. Returns the tone-removed char.
    """
    decomp = unicodedata.normalize("NFD", char)
    base = decomp[0]
    diacs = []
    for p in decomp[1:]:
        if ord(p) in TONE_CODEPOINTS:
            continue
        diacs.append(p)
    new = base + ''.join(diacs)
    return unicodedata.normalize("NFC", new)
def apply_tone(char, combining_codepoint):
    """
    Apply a tone mark to a Vietnamese character (assuming tone already stripped).
    If combining_codepoint = None, return unchanged.
    """
    if combining_codepoint is None:
        return char
    decomp = unicodedata.normalize("NFD", char)
    new = decomp + chr(combining_codepoint)
    return unicodedata.normalize("NFC", new)
def retone_string(s, combining_codepoint):
    """
    For the whole Vietnamese syllable/value:
    - Identify the position of the vowel that originally had the tone
    - Strip existing tone from all chars
    - Apply new tone to the same vowel position (Vietnamese rule: tone stays on the same vowel)
    For your dataset, every value is a single syllable, so one tone per syllable.
    If no original tone, apply to the last character (fallback).
    """
    chars = list(s)
    # Find the position of the char with the original tone
    tone_pos = None
    for i, c in enumerate(chars):
        decomp = unicodedata.normalize("NFD", c)
        has_tone = any(ord(p) in TONE_CODEPOINTS for p in decomp[1:])
        if has_tone:
            tone_pos = i
            break  # Assume only one toned vowel per syllable
    if tone_pos is None:
        # Fallback: apply to last char if no original tone
        tone_pos = len(chars) - 1
    # Strip tones from all chars
    stripped = [strip_tone(c) for c in chars]
    # Apply new tone to the identified position
    if combining_codepoint is not None:
        stripped[tone_pos] = apply_tone(stripped[tone_pos], combining_codepoint)
    return ''.join(stripped)
# ---------------------------------------------------------
# Tone pair definitions
# ---------------------------------------------------------
tone_pairs = [
    ("s", "w", 0x0301), # acute
    ("d", "e", 0x0309), # hook above
    ("a", "q", 0x0303), # tilde
    ("k", "i", 0x0300), # grave
    ("", "t", None), # tone removal
]
# ---------------------------------------------------------
# Main transformation
# ---------------------------------------------------------
def process_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    with open(output_path, "w", encoding="utf-8") as out:
        # Write original block
        for ln in lines:
            out.write(ln + "\n")
        # Process tone pairs
        for n1, n2, tone_cp in tone_pairs:
            out.write("\n") # separate blocks
            for ln in lines:
                if "\t" not in ln:
                    out.write(ln + "\n")
                    continue
                key, val = ln.split("\t", 1)
                if not key:
                    out.write(ln + "\n")
                    continue
                final = key[-1]
                # Only transform l and o
                if final == "l":
                    new_key = key[:-1] + n1
                elif final == "o":
                    new_key = key[:-1] + n2
                else:
                    new_key = key
                new_val = retone_string(val, tone_cp)
                out.write(f"{new_key}\t{new_val}\n")
# ---------------------------------------------------------
# Run
# ---------------------------------------------------------
if __name__ == "__main__":
    input_file = "1_.txt"
    output_file = "1_1_.txt"
    process_file(input_file, output_file)