def count_freq(filepath):
    """This method counts the frequency of each word in a file"""
    with open(filepath, 'r') as file:
        lines = file.readlines()
        freq = {}
        for line in lines:
            for word in line.split():
                freq[word] = freq.get(word, 0) + 1 
                """ if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
                """
    return freq



filepath = 'sample.txt'

print(count_freq(filepath))