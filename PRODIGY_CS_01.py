import argparse

# Caesar Cipher with support for letters, digits, and special characters
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift direction for decryption
    if mode == 'decrypt':
        shift = -shift

    # Full ASCII printable character range
    start_ascii = 32
    end_ascii = 126
    total_chars = end_ascii - start_ascii + 1

    for char in text:
        if start_ascii <= ord(char) <= end_ascii:
            shifted_char = chr((ord(char) - start_ascii + shift) % total_chars + start_ascii)
            result += shifted_char
        else:
            # If the character is outside the printable range, leave it unchanged
            result += char

    return result

# Interactive mode for user input
def interactive_mode():
    while True:
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        # Encrypt the message
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
        print(f"Decrypted Message: {decrypted_message}")

        # Ask the user if they want to enter another message
        continue_choice = input("Do you want to enter another message? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher Program with Interactive Mode")

    # Define arguments for text, shift, and mode
    parser.add_argument("-t", "--text", type=str, help="Input text for encryption or decryption")
    parser.add_argument("-s", "--shift", type=int, help="Shift value for Caesar Cipher")
    parser.add_argument("-m", "--mode", choices=['encrypt', 'decrypt'], default='encrypt', help="Mode: encrypt or decrypt")

    # Parse arguments
    args = parser.parse_args()

    # If arguments are provided, use argparse flow
    if args.text and args.shift:
        result = caesar_cipher(args.text, args.shift, args.mode)
        print(f"Result: {result}")
    else:
        # If arguments are not provided, switch to interactive mode
        print("No arguments provided, switching to interactive mode.")
        interactive_mode()
