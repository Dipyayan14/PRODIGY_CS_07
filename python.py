def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
