import pywhatkit as kit
import pandas as pd
from datetime import datetime
from PIL import Image

# Load the contact list from the CSV file
csv_file = 'codes.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Define the message to be sent
message = "இச்சலுகை ரூபாய் ஐந்தாயிறதிர்க்கு ( ₹ 5000) மேல் வாங்கும் தங்கம்/வெள்ளி/வைரம் பொருட்களுக்கு மட்டும் பொருந்து.\nஇச்சலுகை தங்கம் மற்றும் வெள்ளி நாணயங்களுக்குப் பொருந்தாது.\nஇச்சலுகை வேறு எந்த சலுகைகளுடனும் பொருந்தாது.\nசலுகை பெற கடைசி நாள்: 11-11-2023"

# Define the time at which the message should be sent
# Here, we set it to be sent immediately, but you can customize it
now = datetime.now()
send_time = now.replace(second=0, microsecond=0)

i = 1
# Loop through the contact list and send messages
for index, row in df.iterrows():
    contact_number = str(row[0])
    
    try:
        kit.sendwhatmsg(f"+{contact_number}", message, send_time.hour, send_time.minute + 2) 
        print(f"Message sent to {contact_number}.")
        image_path = f"Coupon codes\\coupon_{i}"
        img = Image.open(image_path)

        # Send the image in a separate message
        kit.sendwhatmsg(f"+{contact_number}", img_path=image_path, time_hour=send_time.hour, time_minute=send_time.minute + 2)
        print(f"Image sent to at {contact_number}.")
        i = i+1
    except Exception as e:
        print(f"Failed to send message to {contact_number}")