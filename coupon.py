from PIL import Image

# Load the template image
template = Image.open('template.jpg')

# Specify the folder containing QR code images
qr_code_folder = 'QR_codes/'

# Specify the folder to save the resulting coupon images
output_folder = 'Coupon codes/'

# List all the QR code filenames in the folder
import os
qr_code_files = [f for f in os.listdir(qr_code_folder) if f.endswith('.png')]

for i, qr_code_filename in enumerate(qr_code_files, start=1):
    # Open the QR code image
    qr_img = Image.open(os.path.join(qr_code_folder, qr_code_filename))

    qr_img = qr_img.resize((200, 200))
    # Determine the paste location for each QR code
    x_position = 1100  # Adjust the X coordinate as needed
    y_position = 300  # Adjust the Y coordinate as needed

    # Paste the QR code onto the template
    template.paste(qr_img, (x_position, y_position))

    # Specify the output folder and save the resulting coupon image
    coupon_filename = os.path.join(output_folder, f'coupon_{i}.png')
    template.save(coupon_filename)

# Close the template image
template.close()
