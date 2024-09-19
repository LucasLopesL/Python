# Módulos

import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage

# QR Code com imagem

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr.add_data('https://www.em2it.com/')
imagem = qr.make_image(
    image_factory=StyledPilImage, embeded_image_path='em2_logo.png'
)

imagem.save("qrcode_logo.png")
