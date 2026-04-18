def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    print("Caesar Cipher Program")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice.")
