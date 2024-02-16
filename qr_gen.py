import csv
import qrcode
from PIL import Image
import os
import random
import string

# Function to generate alphanumeric code
def generate_alphanumeric_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

# Function to generate QR codes
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Number of entries
num_entries = 9380

# Output folder for QR codes
output_folder = "QR_codes"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Output CSV file name
csv_filename = "qr_codes.csv"

# Generate QR codes and alphanumeric codes, and save them to the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Entry No", "QR Code", "Status", "Validity"])
    
    for entry_number in range(1, num_entries + 1):
        alphanumeric_code = generate_alphanumeric_code(10)  # Adjust the length as needed
        qr_filename = os.path.join(output_folder, f"qr_code_{entry_number}.png")
        generate_qr_code(alphanumeric_code, qr_filename)
        writer.writerow([entry_number, alphanumeric_code, "NC", "11-11-2023"])
        print(f"Generated QR code for Alphanumeric Code {alphanumeric_code}")

print(f"QR codes and CSV file ({csv_filename}) generated successfully in the '{output_folder}' folder.")
