🕵️ Steganography Project in Python

This project allows you to hide (encode) and extract (decode) secret messages inside images using **Least Significant Bit (LSB)** steganography in **Python**.

---

📌 What is Steganography?

**Steganography** is the practice of hiding information within other non-secret text or data. In this project, secret messages are hidden inside the pixels of an image by modifying their RGB values in a way that is visually undetectable.

---

🚀 Features

- Hide any text message inside an image (`encode.py`)
- Extract hidden text from an image (`decode.py`)
- Works with lossless image formats like `.png`
- Simple command-line based usage

---

🛠️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)

Install required package:

pip install pillow

---

📥 How to Use
🔒 Encode a Message
- Place a .png image in the project directory named input.png (or change the filename in encode.py).

- Run the encoder script:
python encode.py

- Enter the message you want to hide when prompted.

- The script will create output.png with the hidden message.

🔓 Decode a Message
- Run the decoder script on the output.png file:
python decode.py

- It will extract and display the hidden message.

---

⚠️ Important Notes
Always use PNG or other lossless formats. Do not use .jpg, as it compresses the image and may corrupt the hidden data.

Do not edit or re-save output.png in apps like Paint or WhatsApp — they may alter pixel data and break decoding.

You can share output.png with someone else, and they can decode it with decode.py.
