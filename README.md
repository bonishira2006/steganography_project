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

```bash
pip install pillow
