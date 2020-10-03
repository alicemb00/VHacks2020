# Name: Ethan Nguyen
# VUnetID: nguyeneh 
# Email: ethan.h.nguyen@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 01
# Date: 2/28/2020
# Honor statement: I attest that I understand the honor code for this class and have neither given 
#                  nor received any unauthorized aid on this assignment.

# Program description: This program asks for a plaintext and running key. The program will encrypt 
#                       the plaintext print the cipher text. It will also print the original
#                       plaintext based on the on performing the decryption of the ciphertext.  

'''
The intro() function asks the user for a plaintext and running key.

@return text, key   The function returns the plain text and running key. 
'''
def intro():

    # Ask the user for input on text
    text = input('Enter text (letters only): ')
    text = check_letters_only(text) # Check if the string is valid.

    # Repeat above but for running key
    key = input('Enter key (letters only): ')
    key = check_letters_only(key)
    print()

    return text, key

'''
The check_letters_only(check_me) function will verify if a string contains valid type of characters.

@parameter  check_me    The plaintext string to check if it is valid.
@return                 After prompting the user again, the valid plaintext string is returned.
'''
def check_letters_only(check_me):
    check_me = check_me.lower()
    # Set-up a condition for a while loop.
    error = 1 
    while error != 0:
        error = 0
        for char in check_me: 
            # If statement checks if characters is valid. If not, change error to one.
            if (char < 'a') or (char > 'z'):
                error = 1
        # If the plaintext is invalid, then ask for a new input.
        if error == 1:
            check_me = input('Input must contain only letters. Try again: ')
            check_me = check_me.lower()
    return check_me

'''
The encrypt(text, key) function will encrypt the plaintext using the key.

@parameter  text        The plaintext that the function needs to encrypt.
@parameter  key         The running key the function uses to encrypt.
@parameter  option      When option = 1, encrypt. When option = 2, decrypt
@return                 The encrypted plain text
'''
def encrypt(text, key, option = 1):
    # Set-up variables for while loop.
    password = '' # Stores the encrypted text

    # Use while loop to iterate and encrypt each character.
    for idx in range(len(text)):
        if option == 1:
            cipher = (((ord(text[idx])-97) + (ord(key[idx])-97)) % 26)
        if option == 2:
            cipher = (((ord(text[idx])-97) - (ord(key[idx])-97)) % 26)
        cipher = (chr(cipher + 97))
        password = password + cipher # Add encrypted character to password.
    
    return password
    
def main():
    # Set-up setinel loop.
    stop = ''
    while stop != 'n':
        (text, key) = intro() # Ask for text and key to encrypt

        password = encrypt(text, key) # Encrypt text
        print(f'The encoded text: {password}')

        original = encrypt(password, key, option = 2) # Decrypt password
        print(f'The decoded text: {original}')
        print()
        
        stop = input('Run again? ')

# DO NOT CHANGE ANYTHING BELOW THIS COMMENT.
if __name__ == '__main__':
    main() 

