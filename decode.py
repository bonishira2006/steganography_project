from PIL import Image

def decode_message(img_path):
    img = Image.open(img_path)
    pixels = list(img.getdata())

    binary_data = ""
    for pixel in pixels:
        for color in pixel[:3]:  # R, G, B
            binary_data += str(color & 1)

    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == '00000000':  # end of message
            break
        message += chr(int(byte, 2))

    print("🔓 Hidden message:", message)

# Example usage
decode_message("output.png")
