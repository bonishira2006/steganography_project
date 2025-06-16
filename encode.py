from PIL import Image

def message_to_binary(message):
    return ''.join([format(ord(char), '08b') for char in message])

def encode_message(img_path, message, output_path):
    img = Image.open(img_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    binary_msg = message_to_binary(message) + '00000000'  # 8 zero bits = end of message
    pixels = list(img.getdata())

    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if msg_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    print("✅ Message hidden successfully in", output_path)

# Example usage
secret_message = input("Enter the message to hide: ")
encode_message("input.png", secret_message, "output.png")
