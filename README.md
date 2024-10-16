Overview
This is a simple Caesar Cipher program implemented in Python that allows users to encrypt and decrypt text using a shift key. The program supports both lowercase letters and spaces, providing a straightforward command-line interface for user interaction.

Key Features
Encryption: Scrambles the input text by shifting each letter by a specified key.
Decryption: Restores the original text by reversing the shift using the same key.
User-Friendly Interface: Provides a simple command-line prompt for selecting encryption or decryption modes and entering the key and text.
Usage
Launch the program: Run the Python script in a terminal or command prompt.
Select Mode:
Enter e for encryption or d for decryption.
Input the Key: Enter a numeric key between 1 and 26.
Enter the Text: Provide the text to be encrypted or decrypted.
Output: The program will display the resulting ciphertext or plaintext.
Example:
Encryption:
Input: e, Key: 3, Text: hello
Output: ciphertext is khoor
Decryption:
Input: d, Key: 3, Text: khoor
Output: plaintext: hello
How It Works
Encryption: Each letter in the plaintext is shifted by the specified key. If the shift goes beyond z, it wraps around to the beginning of the alphabet.
Decryption: Each letter in the ciphertext is shifted back by the same key to retrieve the original plaintext.
