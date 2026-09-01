# 🔐 Caesar Cipher

A simple and educational **Python implementation of the Caesar Cipher encryption and decryption technique**.

The project demonstrates fundamental programming concepts such as string manipulation, loops, conditional statements, character encoding, modular arithmetic, and command-line interaction.

> ⚠️ **Educational Project:** Caesar Cipher is not secure for real-world data protection. It is included here only for learning basic cryptography concepts.

---

## ✨ Features

* 🔒 Encrypt text using a custom shift value
* 🔓 Decrypt encrypted messages
* 🔢 Supports positive and negative shifts
* 🔄 Supports shift values greater than 26
* 🔠 Preserves uppercase and lowercase letters
* 🔤 Supports English alphabet characters
* ␠ Preserves spaces
* 🔣 Preserves numbers and punctuation
* 💻 Simple command-line interface
* 📦 Uses only the Python standard library
* 🧩 Separate encryption and decryption functions

---

## 🧠 What is Caesar Cipher?

The **Caesar Cipher** is one of the oldest and simplest substitution ciphers.

It encrypts a message by shifting each alphabetic character by a fixed number of positions.

For example, with a shift of **3**:

```text
A → D
B → E
C → F
```

So:

```text
Hello World
```

becomes:

```text
Khoor Zruog
```

The same shift can be reversed to decrypt the message.

---

## ⚙️ How It Works

The English alphabet contains **26 letters**.

For encryption:

```text
encrypted_position = (original_position + shift) % 26
```

For decryption:

```text
decrypted_position = (original_position - shift) % 26
```

The `% 26` operation keeps the character inside the alphabet.

For example:

```text
X + 3 → A
Y + 3 → B
Z + 3 → C
```

The program also preserves the original letter case.

---

## 🛠️ Technology Stack

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python 3.8+             | Programming language           |
| Python Standard Library | Character and input processing |
| Git                     | Version control                |
| GitHub                  | Source-code hosting            |

---

## 📁 Project Structure

```text
PRODIGY_CS_01/
│
├── caesar_cipher.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📋 Requirements

* Python **3.8 or newer**
* Git (optional, for cloning the repository)
* No external Python packages are required

Check your Python version:

```bash
python --version
```

On some systems:

```bash
python3 --version
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/jeevicyber28/PRODIGY_CS_01.git
```

Move into the project directory:

```bash
cd PRODIGY_CS_01
```

No additional dependencies are required.

---

## ▶️ Running the Program

Run:

```bash
python caesar_cipher.py
```

Or:

```bash
python3 caesar_cipher.py
```

The program will display an interactive menu where you can choose between encryption and decryption.

---

## 🔒 Encryption Example

Choose encryption:

```text
Type 'e' to encrypt or 'd' to decrypt: e
```

Enter your message:

```text
Enter your message: Hello World
```

Enter the shift:

```text
Enter shift value: 3
```

Output:

```text
Encrypted message: Khoor Zruog
```

---

## 🔓 Decryption Example

Choose decryption:

```text
Type 'e' to encrypt or 'd' to decrypt: d
```

Enter the encrypted message:

```text
Enter your message: Khoor Zruog
```

Enter the shift:

```text
Enter shift value: 3
```

Output:

```text
Decrypted message: Hello World
```

---

## 🔤 Character Handling

The program handles different types of characters without changing their intended format.

### Letters

```text
Hello → Khoor
HELLO → KHOOR
```

### Spaces and punctuation

```text
Hello, World! → Khoor, Zruog!
```

### Numbers

```text
Hello 123 → Khoor 123
```

Non-alphabetic characters such as spaces, numbers, and punctuation remain unchanged.

---

## 🧩 Using the Functions Directly

The encryption and decryption functions can also be imported into another Python program:

```python
from caesar_cipher import caesar_encrypt, caesar_decrypt

message = caesar_encrypt("Hello", 3)
print(message)

original = caesar_decrypt(message, 3)
print(original)
```

Output:

```text
Khoor
Hello
```

---

## 🧪 Example Test Cases

The following cases can be used to test the implementation:

```python
assert caesar_encrypt("ABC", 3) == "DEF"
assert caesar_encrypt("xyz", 3) == "abc"
assert caesar_encrypt("Hello, World!", 3) == "Khoor, Zruog!"
assert caesar_decrypt("Khoor", 3) == "Hello"
assert caesar_encrypt("Python", 0) == "Python"
```

Recommended cases to test:

* Lowercase text
* Uppercase text
* Mixed-case text
* Empty strings
* Shift value `0`
* Shift value `26`
* Shift values greater than `26`
* Negative shift values
* Spaces
* Numbers
* Punctuation
* Invalid menu choices
* Invalid shift values

---

## ⚠️ Security Notice

**Caesar Cipher should NOT be used for real-world security.**

There are only **26 possible shifts** in the standard English alphabet, making the cipher extremely easy to brute-force.

Do not use this implementation to protect:

* Passwords
* API keys
* Financial information
* Personal information
* Confidential files
* Authentication credentials

For real security applications, use modern, peer-reviewed cryptographic algorithms and established cryptography libraries.

---

## 🚧 Limitations

* Supports the English alphabet only
* Vulnerable to brute-force attacks
* Does not use a secret cryptographic key
* Does not provide authentication
* Does not provide integrity protection
* Not suitable for production security
* Does not encrypt files or network traffic

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add stronger input validation
* [ ] Add automated unit tests
* [ ] Add a menu loop for multiple operations
* [ ] Add a graphical user interface
* [ ] Add command-line arguments using `argparse`
* [ ] Add GitHub Actions for automated testing
* [ ] Add support for custom alphabets
* [ ] Add clearer error messages
* [ ] Add more test cases
* [ ] Improve user experience

---

## 🤝 Contributing

Contributions are welcome for educational improvements.

To contribute:

```bash
git checkout -b improve-caesar-cipher
```

Make your changes, test them locally, and commit:

```bash
git add .
git commit -m "Improve Caesar Cipher validation"
```

Push your branch:

```bash
git push origin improve-caesar-cipher
```

Then open a Pull Request on GitHub.

---

## 🛡️ Safe Development Practices

* Never commit passwords or API keys
* Never commit confidential information
* Use synthetic data in examples and tests
* Review changes before pushing
* Keep commit messages clear and meaningful
* Do not describe Caesar Cipher as secure encryption

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

## 👨‍💻 Author

**Jeevicyber28**

GitHub Repository:

https://github.com/jeevicyber28/PRODIGY_CS_01

---

## 🙏 Acknowledgements

This project is based on the classical **Caesar Cipher**, traditionally associated with Julius Caesar.

It is implemented here for educational purposes to demonstrate basic cryptography and programming concepts.

---

## ⭐ Final Note

This project is designed to help beginners understand:

* Basic cryptography
* String manipulation
* Functions
* Loops
* Conditional statements
* Character encoding
* Modular arithmetic
* Input handling
* Testing
* Git and GitHub workflows
## 📌 Project Highlights

This project demonstrates the fundamentals of the Caesar Cipher algorithm, including encryption, decryption, modular arithmetic, and string processing.

If you find this project useful, consider giving the repository a ⭐.
