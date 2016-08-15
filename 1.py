def most_frequent(text):
    frequencies = [(c, text.count(c)) for c in set(text)]
    return [max(frequencies, key=lambda x: x[1])[0], min(frequencies, key=lambda x: x[1])[0]]

def  find_chars( st):
    str = "aaabaabcccccc"
    occurencies = [(char, str.count(char)) for char in set(str)]
    return [max(occurencies, key=lambda x: x[1])[0], min(occurencies, key=lambda x: x[1])[0]]


s = 'ABBCCCDDDD'
print(find_chars(s))