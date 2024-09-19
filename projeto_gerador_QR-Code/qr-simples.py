# Módulos

import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage

# QR Code Simples

imagem = qrcode.make('https://www.linkedin.com/in/lucas-lopes-40b02522b/')
imagem.save("qrcode.png")
