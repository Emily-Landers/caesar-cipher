from corpus_loader import word_list, name_list

def encrypt(string, key):
	newLetters = []
	newKey = key % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)
def getNewLetter(letter, key):
    if letter == " ":
        return " "
    elif ord(letter) > 64:
        newLetterCode = ord(letter) + key
        print(newLetterCode)
        return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)
    else:
        return letter

def decrypt(encrypted, key):
    newLetters = []
    newKey = key % 26
    for letter in encrypted:
        newLetters.append(getNewLetters(letter, newKey))
    return "".join(newLetters)
def getNewLetters(letter, key):
    if letter == " ":
        return " "
    elif ord(letter) > 64:
        newLetterCode = ord(letter) - key
        print(newLetterCode)
        return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)
    else:
        return letter

def crack(text):
    candidates = []
    for phrase in range(26):
        candidates.append(encrypt(text, phrase))

    for i in candidates:
        word_count = count_words(phrase)
        percentage = int(word_count / len(i.split()) * 100)
        if percentage > 50:
            return phrase
    return ""

def count_words(text):
    # returns a count of real words
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass

    return word_count


           