
def count_lines_words_chars(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(lines)
        number_of_lines = len(lines)
        words = sum(len(line.split()) for line in lines)
        chars = sum(len(word) for word in lines)

    return number_of_lines, words, chars

l, w, c = count_lines_words_chars("sample.txt")

print(f"lines: {l}\nwords: {w}\nchars: {c}")

answer = count_lines_words_chars("sample.txt")
print(answer)