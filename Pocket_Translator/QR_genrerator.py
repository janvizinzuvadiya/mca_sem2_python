import qrcode # pip install qrcode[pil]

# 1. PASTE YOUR LINK HERE
my_link = "https://gist.github.com/janvizinzuvadiya/778f3e7f8bb052a972d6e656ab40421c" 

# 2. Setup the QR style
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(my_link)
qr.make(fit=True)

# 3. Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_poster_qr.png")

print("Success! 'my_poster_qr.png' is ready to be printed and glued to your chart.")