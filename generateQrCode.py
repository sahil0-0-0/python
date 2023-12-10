import qrcode
# paste link of web site to create QrCOde
qr = qrcode.make("https://www.w3schools.com/")

# write file name to save QrCode jpg image
qr.save("w3.jpg")