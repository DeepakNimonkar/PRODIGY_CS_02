from PIL import Image
import os

def encrypt_decrypt_image(image_path, key, mode):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Simple XOR operation on each pixel value
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    output_path = ""
    if mode == "encrypt":
        output_path = "encrypted_image.png"
    else:
        output_path = "decrypted_image.png"

    img.save(output_path)
    print(f"{mode.title()}ion complete. Saved as {output_path}")


def main():
    print("Simple Image Encryption Tool By : Deepak")
    print()
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Choose an option (1/2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice!")
        return

    image_path = input("Enter image path: ").strip()
    if not os.path.exists(image_path):
        print("Image file does not exist!")
        return

    try:
        key = int(input("Enter encryption key (0-255): "))
        if key < 0 or key > 255:
            raise ValueError
    except ValueError:
        print("Invalid key! Must be an integer between 0 and 255.")
        return

    mode = "encrypt" if choice == "1" else "decrypt"
    encrypt_decrypt_image(image_path, key, mode)


if __name__ == "__main__":
    main()
