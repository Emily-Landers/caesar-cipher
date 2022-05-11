
def encrypt():
    pass

def decrypt():
    pass
def crack():
    pass







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
           