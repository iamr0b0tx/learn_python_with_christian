import string

file = open('file.txt')
contents = file.read()

unwanted_chr = list(string.punctuation)
unwanted_chr.remove("'")
unwanted_chr.append('\n')

for unwanted_ch in unwanted_chr:
    contents = contents.replace(unwanted_ch, '')
    
counter = {}
words = contents.split()
unique_words = set(words)

for unique_word in unique_words:
    frequency = words.count(unique_word)
    counter[unique_word] = frequency
    print(f'{unique_word:18s} {frequency}')
    
file.close()
