with open("books/frankenstein.txt") as f:
    file_contents = f.read().lower()
    
    words = file_contents.split()
    word_count = len(words)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    letters = {}

    for word in words:
        for letter in word:
            if letter in abc:
                if letter not in letters:
                    letters[letter] = 1
                elif letter in letters:
                    letters[letter] += 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for letter in letters:
        print(f"The '{letter}' was found {letters[letter]} times")

    print("--- End Report ---")


