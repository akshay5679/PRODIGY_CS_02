from PIL import Image

def encrypt_image(input_image_path, output_image_path, shift):
    image = Image.open(input_image_path)
    pixels = image.load()
    """
██████░▄██▄▄██▄░▄████▄░▄██████░▄█████
░░██░░░██░██░██░██░░██░██░░░░░░██░░░░
░░██░░░██░██░██░██░░██░██░░███░█████░
░░██░░░██░██░██░██████░██░░░██░██░░░░
██████░██░██░██░██░░██░▀█████▀░▀█████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + shift) % 256, (g + shift) % 256, (b + shift) % 256)

    image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, shift):
    image = Image.open(input_image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - shift) % 256, (g - shift) % 256, (b - shift) % 256)

    image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    input_image_path = input(r"D:\input.jpg").strip()
    output_image_path = input(r"D:\outimg.jpg").strip()
    shift = int(input("Enter shift value: ").strip())

    if mode == "encrypt":
        encrypt_image(input_image_path, output_image_path, shift)
    elif mode == "decrypt":
        decrypt_image(input_image_path, output_image_path, shift)
    else:
        print("Invalid mode selected. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

