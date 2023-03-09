from pyqrcode import QRCode
import pyqrcode


# model1

# String which represent the QR code
mystring = "avalanch"

# Generate QR code
qr1 = pyqrcode.create(mystring)

# Create and save the png file naming "qrcode.png"
qr1.svg("qrcode.svg", scale=8)

# ---------------------------------------------------------
# model 2

s = 'avalanch'
myqr = QRCode(s)
# myqr.show()

# save qrcode
myqr.png('qrcode2.png', scale=8)

# --------------------------------------------------------
# custom qrcode

url = 'https://github.com/bahmanpnn'

myQR = QRCode(url, error='H', version=None, mode=None, encoding='iso-8859-1')

myQR.png('customqr.png', scale=8)

# url: is clear that is your content that you want to convert to qrcode

# error: is accurancy correction level that try to correct our code.It is set to "H" by default.

# version: Specifies the size and data capacity of the code (it can take integer values between 1 and 40) and
# when left unspecified,finds the smallest possible QR code version to store the data we want (knowing its size)

# mode: Specifies how to encode the content (there are four options: numeric, alphanumeric, binary, kanji).
# If left unspecified, it is guessed by the algorithm.

# encoding: Specifies how to encode the content and defaults to iso-8.

# for more informations check this source: https://pythonhosted.org/PyQRCode/moddoc.html
