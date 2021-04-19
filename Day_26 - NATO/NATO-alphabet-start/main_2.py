import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data.to_dict())
# print(nato_dict)
word = input('Enter a word: ').upper()
# print(word)
nato_spelling = [nato_dict[letter] for letter in word]
print(nato_spelling)
