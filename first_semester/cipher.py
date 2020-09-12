# Cipher

# Write a Java program which converts (user entered) plain text to cipher text using a substitution cipher 
# (in which plain text letters are randomly assigned to cipher text letters). 
# Note that a Substitution Cipher replaces plaintext with cipher-text.
# The most common substitution ciphers replace single characters of plaintext with predefined single characters of cipher-text 
# (e.g. the plain-text character `a' might be replaced by cipher text character 'q', 'b' might be replaced by 'x', 'c' by 'k' and so on).  
#  Each plain-text character should be replaced by a different cipher-text character.
# As part of your solution you must write and use at least the following functions/methods:
# (i)    createCipher() which determines and returns the mapping from plain text to cipher text.  Each plain text character ('a' .. 'z', ' ') must be randomly assigned a cipher-text character;
# (ii)   an encrypt() method which takes a plain text phrase (as an array of characters) & the cipher and returns an encrypted version of the phrase according to the substitution cipher;
# (iii)  crypt() which takes an encrypted phrase (as an array of characters) & the cipher mapping and returns a plain text version of the phrase according to the substitution cipher

# Hints:
# A 27 element 1-D array (26 letters and the space character) can be used for the mapping where each element is the cipher-text character corresponding to a particular letter.
# Given a String called myString you can create an array of characters as follows:
# char[] characterArray = myString.toCharArray();
# To convert back to a String:
# String anotherString = new String( characterArray );
# To convert a String to lowercase:
# String lowercaseString = myString.toLowerCase();
import string
import random
import pdb
# pdb.set_trace()

# NOTE: This assignment was compeleted by using a dictionary as a cipher rather than a 2D-array

def create_cipher():
	# list containing the letters of the alphabet and the space character
	ordered_alpha = list(string.ascii_lowercase + ' ')
	# randomly shuffeld alphabet list
	shuffled_alpha = list(string.ascii_lowercase + ' ')
	random.shuffle(shuffled_alpha)
	# cipher is a dictionary with {"letter":"random letter"} key:value pairs
	cipher = {}
	for index,letter in enumerate(ordered_alpha):
		cipher[letter] = shuffled_alpha[index]
	return cipher

def encrypt(text, cipher):
	encrypted_text = ""
	for letter in text:
		encrypted_text = encrypted_text + cipher[letter]
	return encrypted_text

def crypt(encrypted_text, cipher):
	decrypted_text = ""
	for letter in encrypted_text:
		for key, value in cipher.items(): 
			if letter == value: 
				decrypted_text = decrypted_text + key
	return decrypted_text
		

cipher = create_cipher()
text_to_encrypt = input("Enter text to encrypt: ").lower()
print(f"Cipher:\n {cipher}")
encrypted_text = encrypt(text_to_encrypt, cipher)
print("Encrypted text: " + encrypted_text)
decrypted_text = crypt(encrypted_text, cipher)
print("Decrytped text: " + decrypted_text)
