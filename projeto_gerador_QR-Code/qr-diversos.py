# Módulos

import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage

# Diversos QR Code ao mesmo tempo

redes_sociais = {
    "LinkedIn": "https://www.linkedin.com/in/lucas-lopes-40b02522b/",
    "GitHub": "https://github.com/LucasLopesL"
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q)
    qr.add_data(url)
    qr.save(f"sociais{rede_social}.png")
