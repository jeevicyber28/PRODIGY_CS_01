Caesar Cipher

A simple and educational Python implementation of the Caesar Cipher encryption technique.





























Overview

The Caesar Cipher is one of the oldest and simplest substitution ciphers.

It encrypts a message by shifting every alphabetic character by a fixed number of positions in the alphabet.

For example, with a shift value of 3:

Plain Text


A becomes D
B becomes E
C becomes F



The same shift can be reversed to decrypt the message.

This project provides a small command-line program written in Python.

It is intended for learning programming, text processing, and basic cryptography concepts.

Project Goals

This project was created to demonstrate the following concepts:

•
Python functions.

•
Loops and conditional statements.

•
String processing.

•
Character encoding with ord() and chr().

•
Modular arithmetic.

•
Command-line user input.

•
Basic encryption and decryption logic.

•
Case preservation.

•
Handling of spaces and punctuation.

Features

The program includes the following features:

•
Encrypts a plain-text message.

•
Decrypts an encrypted message.

•
Accepts positive shift values.

•
Supports negative shift values.

•
Supports shift values larger than 26.

•
Preserves uppercase letters.

•
Preserves lowercase letters.

•
Leaves spaces unchanged.

•
Leaves numbers unchanged.

•
Leaves punctuation unchanged.

•
Provides a simple interactive command-line interface.

•
Uses separate functions for encryption and decryption.

•
Requires no third-party Python packages.

Important Security Notice

This implementation is designed for education and experimentation.

The Caesar Cipher is not secure for protecting passwords, personal information, API keys, financial data, or confidential files.

There are only 26 possible shifts in the standard English alphabet.

An attacker can try every possible shift very quickly.

Do not use this program to protect real-world sensitive information.

Use modern, peer-reviewed cryptographic libraries for real security applications.

Technology Stack

Technology
Purpose
Python
Application programming language
Standard library
Character and input processing
Git
Version control
GitHub
Source-code hosting and collaboration




Repository Structure

Plain Text


PRODIGY_CS_01/
├── caesar_cipher.py
├── .gitignore
├── LICENSE
└── README.md



Requirements

You need Python 3.8 or a newer version.

No external packages are required to run the program.

You can check whether Python is installed by running:

Bash


python --version



On some systems, use:

Bash


python3 --version



Installation

Clone this repository using Git:

Bash


git clone https://github.com/jeevicyber28/PRODIGY_CS_01.git



Move into the project directory:

Bash


cd PRODIGY_CS_01



The program is ready to run after cloning.

A virtual environment is optional because the project uses only the Python standard library.

Running the Program

Run the script with the following command:

Bash


python caesar_cipher.py



On systems where Python 3 is available through python3, use:

Bash


python3 caesar_cipher.py



The program will display an interactive menu.

You will be asked whether you want to encrypt or decrypt a message.

You will then enter the message and the shift value.

Encrypting a Message

Start the program:

Bash


python caesar_cipher.py



Choose the encryption option:

Plain Text


Type 'e' to encrypt or 'd' to decrypt: e



Enter a message:

Plain Text


Enter your message: Hello World



Enter a shift value:

Plain Text


Enter shift value: 3



The output will be:

Plain Text


Encrypted message: Khoor Zruog



Decrypting a Message

Run the program again:

Bash


python caesar_cipher.py



Choose the decryption option:

Plain Text


Type 'e' to encrypt or 'd' to decrypt: d



Enter the encrypted message:

Plain Text


Enter your message: Khoor Zruog



Enter the same shift value:

Plain Text


Enter shift value: 3



The output will be:

Plain Text


Decrypted message: Hello World



How the Algorithm Works

The English alphabet contains 26 letters.

The program assigns each letter a position using its character code.

For encryption, the shift value is added to the current character position.

The modulo operator % 26 keeps the result inside the alphabet.

The general encryption formula is:

Plain Text


encrypted_position = (original_position + shift ) % 26



The decryption operation uses the opposite shift:

Plain Text


decrypted_position = (original_position - shift) % 26



The implementation performs decryption by calling the encryption function with a negative shift.

This avoids duplicating the character transformation logic.

Handling Uppercase and Lowercase Letters

Uppercase letters are processed using the range beginning at A.

Lowercase letters are processed using the range beginning at a.

This allows the program to preserve the original case of every letter.

For example:

Plain Text


Hello becomes Khoor with a shift of 3.
HELLO becomes KHOOR with a shift of 3.



Handling Non-Alphabetic Characters

Characters that are not alphabetic are copied without modification.

This includes:

•
Spaces.

•
Numbers.

•
Periods.

•
Commas.

•
Exclamation marks.

•
Question marks.

•
Symbols.

Example:

Plain Text


Hello, World! 123



With a shift of 3, the result is:

Plain Text


Khoor, Zruog! 123



Using the Functions Directly

The functions can also be imported into another Python file:

Python


from caesar_cipher import caesar_encrypt, caesar_decrypt

message = caesar_encrypt("Hello", 3)
print(message)

original = caesar_decrypt(message, 3)
print(original)



Expected output:

Plain Text


Khoor
Hello



Error Handling

The interactive program expects the shift value to be an integer.

For example, this is valid:

Plain Text


Enter shift value: 5



This is not valid:

Plain Text


Enter shift value: three



Future versions may add clearer validation for invalid input values.

Testing Ideas

The following cases should be tested when improving the project:

•
Encrypt a normal lowercase message.

•
Encrypt a normal uppercase message.

•
Encrypt a mixed-case message.

•
Decrypt an encrypted message.

•
Use a shift of zero.

•
Use a shift of 26.

•
Use a shift larger than 26.

•
Use a negative shift.

•
Process spaces and punctuation.

•
Process numbers.

•
Enter an invalid menu option.

•
Enter an invalid shift value.

Example Test Cases

Python


assert caesar_encrypt("ABC", 3) == "DEF"
assert caesar_encrypt("xyz", 3) == "abc"
assert caesar_encrypt("Hello, World!", 3) == "Khoor, Zruog!"
assert caesar_decrypt("Khoor", 3) == "Hello"
assert caesar_encrypt("Python", 0) == "Python"



Limitations

The program supports the English alphabet only.

It does not provide password protection.

It does not use a secret key.

It does not prevent brute-force attacks.

It does not provide authentication.

It does not encrypt files or network traffic.

It does not provide integrity checking.

It should not be used for production security.

Possible Future Improvements

Potential improvements include:

•
Add input validation for the shift value.

•
Add a menu loop for multiple operations.

•
Add unit tests using pytest.

•
Add a graphical user interface.

•
Add file encryption and decryption for learning purposes.

•
Add support for custom alphabets.

•
Add support for Unicode text with clear documentation.

•
Add command-line arguments using argparse.

•
Add continuous integration with GitHub Actions.

•
Add examples for negative shifts.

•
Add a clearer error message for invalid choices.

Contributing

Contributions are welcome for educational improvements.

Before making a change, create a separate branch:

Bash


git checkout -b improve-caesar-cipher



Make a focused change and test it locally.

Use a clear commit message:

Bash


git commit -m "Add input validation for shift values"



Push the branch and open a Pull Request on GitHub.

Please keep contributions respectful, focused, and related to the project.

Safe Development Practices

Do not commit passwords, API keys, private messages, or confidential data.

Do not describe the Caesar Cipher as secure encryption.

Use synthetic examples in documentation and tests.

Review code changes before pushing them to GitHub.

License

This project is licensed under the MIT License.

See the LICENSE file for the complete license text.

Author

Developed as an educational cybersecurity and Python programming project.

Repository: jeevicyber28/PRODIGY_CS_01

Acknowledgements

This project is based on the classical Caesar Cipher technique traditionally associated with Julius Caesar.

It is included here for educational purposes and should not be considered a modern cryptographic system.

Final Notes

The main purpose of this project is to understand how a basic substitution cipher works.

It also demonstrates how a small Python program can be documented, tested, version-controlled, and shared through GitHub.

If you improve this project, update the README so other learners can understand the new behavior.

