# Módulos

import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage

# QR Code Simples

imagem = qrcode.make('https://www.linkedin.com/in/lucas-lopes-40b02522b/')
imagem.save("qrcode.png")

# QR Code com imagem

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
qr.add_data('https://www.em2it.com/')
imagem2 = qr.make_image(
    image_factory=StyledPilImage, embeded_image_path='em2_logo.png'
)

imagem2.save("qrcode_logo.png")

# Diversos QR Code ao mesmo tempo

redes_sociais = {
    "LinkedIn": "https://www.linkedin.com/in/lucas-lopes-40b02522b/",
    "GitHub": "https://github.com/LucasLopesL"
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
    qr.add_data(url)
    imagem3 = qr.make_image()
    imagem3.save(f"sociais{rede_social}.png")


