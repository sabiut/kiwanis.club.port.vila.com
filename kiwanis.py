import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# Create a custom formatted string
custom_data = """KIWANISINFO:
KIWANIS CLUB OF PORT VILA

Bank: BSP
Swift: BOSPVUVX
BSB: 039033
Acc: 2000 359154

REFERENCE:
Please include your name if you are an individual, the table name if you have booked as a group, or your organization name as the payment reference.

Thank you for your support!
"""

# Create QR code instance
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

# Add the custom data
qr.add_data(custom_data)
qr.make(fit=True)

# Create an image from the QR code with rounded modules
qr_image = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

# Convert the QR code to RGB mode
qr_image = qr_image.convert("RGB")

# Open the Kiwanis Port Vila logo
logo = Image.open("kiwanis_port_vila_logo.jpg")

# Calculate the size of the logo (reduced to 15% of the QR code size)
logo_size = int(qr_image.size[0] * 0.15)
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate position to paste the logo (center of QR code)
pos = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)

# Create a white square background for the logo
background = Image.new('RGB', (logo_size, logo_size), 'white')
background.paste(logo, (0, 0), logo if logo.mode == 'RGBA' else None)

# Paste the logo with background onto the QR code
qr_image.paste(background, pos)

# Save the final image
qr_image.save("kiwanis_club_qr_with_logo_custom.png")

print("QR code with Kiwanis Port Vila logo has been generated and saved as 'kiwanis_club_qr_with_logo_custom.png'")