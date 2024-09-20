class WordCounter:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = []
        current_word = ""
        for char in self.text:
            if char != " ":
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""

        if current_word:
            words.append(current_word)

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1 
            else:
                word_count[word] = 1

        return word_count

