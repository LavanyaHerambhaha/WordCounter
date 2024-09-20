from counter import WordCounter
import os


def main():
    subfolder_path = os.path.join('subfolder', 'input.txt')
    with open(subfolder_path, 'r') as file:
        content = file.read()
    word_counter = WordCounter(content)

    word_counts = word_counter.count_words()

    for word, count in word_counts.items():
        print(f"({word} ,{count})")


if __name__ == '__main__':
    main()
