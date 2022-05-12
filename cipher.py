from corpus_loader import word_list

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

def alphabet():
    # letters of alphabet (English)
    letters = "abcdefghijklmnopqrstuvwxyz"
    return(letters)

def crack(encrypted):
# encrypted string to brute force
    best_match = 0
    best_match_text = ""
    best_cipher = 0
    # loop to brute
    x = 0
    while x < 26:
        x = x + 1 
        stringtodecrypt=encrypted
        stringtodecrypt=stringtodecrypt.lower()
        ciphershift=int(x)
        stringdecrypted=""
        letters = alphabet()
        for character in stringtodecrypt:
            position = letters.find(character)
            newposition = position-ciphershift
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            else:
                stringdecrypted = stringdecrypted + character

        detected_words = 0
    
        for word in stringdecrypted.split(' '):
            word = word.strip(" ")
            word = word.strip(",")
            if word in word_list:
                detected_words = detected_words + 1

        if detected_words > best_match:
            best_match_text = stringdecrypted
            best_cipher = str(ciphershift)
            number_of_detected_words = detected_words

    result = "Best matched text:",best_match_text,"With Ciphershift of:",best_cipher," And",number_of_detected_words,"detected words."
    return(result)

# answer = crack(encrypted)
# print(answer)





# import random
# def encrypt(plain, shift):
#     encrypted_text = ""
    
#     for char in plain:
#         num = int(char) #turn string into int
#         shifted_num = (num + shift) % 10 #new number will be the number, plus given shift, remainder 10
#         encrypted_text += str(shifted_num) #add each int back as string 
#     return encrypted_text

# def decrypt(encoded, key):
#     return encrypt(encoded, -key) #will return the opposite of original key to "decrypt"

# if __name__ == "__main__":
#     pins = [
#         "1234",
#         "9876",
#         "0000",
#         "9999"
#     ]
    
#     for pin in pins:
#         key = random.randint(1, 9)
#         print("plain pin", pin, key)
#         encrypted_pin = encrypt(pin, key)
#         print("encrypted_pin", encrypted_pin)
#         decrypted_pin = decrypt(encrypted_pin, key)
#         print("decrypted pin", decrypted_pin)

# import re
# from corpus_loader import word_list, name_list #find install, a corpus is a list of words nltk will need to be downliaded (see demo for syntax)

# candidates = [
#     "a dark and stormy night"
#     "n qnex naq fgbezl avtug"
# ]

# def count_words(text):
#     candidate_words = text.split()#separates words 
#     word_count = 0
#     for candidate in candidate_words: #for loop to add everything
#         word = re.sub(r'[A-Za-z+]', '', candidate) #replaces commas with spaces etc.
#         if word.lower() in word_list or word in name_list: #lowercase all for analysis
#             word_count += 1
#         else:
#             print("not english word or name", word) #will show what is not in word list
#     return word_count    

# for phrase in candidates:
#     word_count = count_words(phrase)
#     percentage = int(word_count / len(phrase.split()) * 100)#calculates what percentage were known words 
#     if percentage > 50:
#         print(phrase, percentage)
        
#isalpha() to determine if its in the alphabet
#get numeric representation for a character by using  ord()
           