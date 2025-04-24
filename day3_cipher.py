def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encode" else -shift
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift_amount) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

# --- Loop Until User Exits ---
while True:
    print("\n🕵️ Welcome to the Secret Message Encoder/Decoder")
    mode = input("Type 'encode' to encrypt or 'decode' to decrypt (or 'exit' to quit): ").lower()

    if mode == "exit":
        print("🔚 Goodbye, agent.")
        break

    message = input("Enter your message: ")
    shift = int(input("Enter shift number (e.g., 3): "))

    encoded_message = caesar_cipher(message, shift, mode)
    print(f"\n🔐 Your {mode}d message: {encoded_message}")
