#!/bin/python3

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)
def encrypt(plaintext,key):
    Ciphertext='' 
    for letter in plaintext:
        letter=letter.lower()
        if not letter == ' ':
            index=letters.find(letter)
            if index == -1 :
                Ciphertext += letter
            else:
                new_index = index + key
                if new_index >=26:
                   new_index -= 26
                Ciphertext += letters[new_index]
    return Ciphertext

def decrypt(ciphertext,key):
    plaintext='' 
    for letter in ciphertext:
        letter=letter.lower()
        if not letter == ' ':
            index=letters.find(letter)
            if index == -1 :
                Ciphertext += letter
            else:
                new_index = index - key
                if new_index < 0:
                   new_index += 26
                plaintext += letters[new_index]
    return plaintext             
        
print("Caeser Sphere program")
print()
print("do you want to encrypt or decrypt")

user = input("e/d: ").lower()
print()

if user == 'e':
   print ("ENCRYPTION MODE SELECTED")
   print()
   key=int(input("Enter the Key(1-26):"))
   text=input("Enter the text to encrypt: ")
   cipher = encrypt(text,key)
   print(f"ciphertext is {cipher}")
elif user =='d':
    print("DECREPTION MODE SELECTION")
    print()
    key=int(input("Enter the Key(1-26):"))
    text=input("Enter the text to decrypt: ")
    plain = decrypt(text,key)
    print(f"plaintext: {plain}")

    
