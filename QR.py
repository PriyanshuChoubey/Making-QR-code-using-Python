import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Hello\nMy name is Priyanshu kumar choubey. \nInstagram ID: https://www.instagram.com/priyanshu__choubey/.")
qr.png("myCode.png", scale=8)


d = decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))