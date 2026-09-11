def is_pangram(sentence):
    seen = set()

    for char in sentence.lower():
        if char.isalpha():
            seen.add(char)

    return len(seen) == 26
