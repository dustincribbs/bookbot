def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(num_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    total_letters = {}
    for char in text.lower():
          if char in total_letters:
              total_letters[char] += 1
          else:
              total_letters[char] = 1
    return total_letters

main()
