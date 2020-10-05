# put your code here.
letter_counts = {}

def word_count(filename):
    text = open(filename)

    for line in text: #prints "Every wife had seven sacks"
        line = line.strip()
        word_list = line.split(" ") #prints: ['As', 'I', 'was', 'going', 'to', 'St.', 'Ives']
        for word in word_list: #loops through each word in the list
            letter_counts[word] = letter_counts.get(word,0) + 1
    return letter_counts

letter_counts = word_count('twain.txt')  
for key, value in letter_counts.items():
    print(" {} {}".format(key, value))

#print(letter_counts)


def make_letter_counts_dict(phrase):
    """Return dict of letters and # of occurrences in phrase."""

    

    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts
letter_counts  = make_letter_counts_dict("test")
# print(letter_counts)