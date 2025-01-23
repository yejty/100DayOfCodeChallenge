import qrcode

# URL to encode
url = input("Give me the URL: ").strip()
image_name = input("Give me a name for the file (without extension): ").strip()

# Generate QR code
qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(url)
qr.make(fit=True)  # Ensure QR is correctly scaled

# Create an image of the QR code
image = qr.make_image(fill_color="#7b552c", back_color ="#eddba8")
image.save(f"{image_name}.png")
print(f"QR code saved as {image_name}.png")
