from spellchecker import spellchecker

def get_file():
    while True:
        try:
            filename = input("Enter the name of the file to spellcheck: ")
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

def spellcheck(file):
    spell = spellchecker("english_words.txt")
    correct_words = 0
    incorrect_words = 0

    for i, line in enumerate(file, 1):
        words = line.strip().split()
        for word in words:
            if not spell.check(word):
                print(f"Incorrect spelling: '{word}' on line {i}")
                incorrect_words += 1
            else:
                correct_words += 1

    total_words = correct_words + incorrect_words
    accuracy = (correct_words / total_words) * 100
    print(f"Summary: Correct words: {correct_words}, Incorrect words: {incorrect_words}, Accuracy: {accuracy:.2f}%")

def main():
    print("Welcome to Spell Checker!")
    file = get_file()
    spellcheck(file)
    file.close()

if __name__ == "__main__":
    main()
