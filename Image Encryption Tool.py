from PIL import Image

def encrypt_image(image_path, key):
    # Remove any leading or trailing quotes and spaces from the image path
    image_path = image_path.strip().strip('"').strip("'")
    
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert image to RGB mode
    img = img.convert('RGB')

    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r ^= key
            g ^= key
            b ^= key
            img.putpixel((x, y), (r, g, b))

    # Save the encrypted image
    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    print("Image encrypted successfully!")
    return encrypted_path

def decrypt_image(encrypted_image_path, key):
    # Remove any leading or trailing quotes and spaces from the image path
    encrypted_image_path = encrypted_image_path.strip().strip('"').strip("'")
    
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Decrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r ^= key
            g ^= key
            b ^= key
            img.putpixel((x, y), (r, g, b))

    # Save the decrypted image
    decrypted_path = encrypted_image_path.split('_encrypted.png')[0] + '_decrypted.png'
    img.save(decrypted_path)
    print("Image decrypted successfully!")
    return decrypted_path

def main():
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    choice = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()

    if choice == 'e':
        encrypted_path = encrypt_image(image_path, key)
        print("Encrypted image saved as:", encrypted_path)
    elif choice == 'd':
        decrypted_path = decrypt_image(image_path, key)
        print("Decrypted image saved as:", decrypted_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
