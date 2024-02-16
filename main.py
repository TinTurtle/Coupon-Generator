import csv
import datetime
import tkinter as tk
from tkinter import messagebox


x = datetime.datetime.now()

def load_csv(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def scan_qr():
    code = entry_code.get()
    updated_value = "C"
    csv_filename = "details.csv"

    if not code:
        messagebox.showerror("Error", "Please enter Valid Code")
        return

    data = load_csv(csv_filename)
    found = False
    for row in data:
        if code in row[1]:  # Check if code is in the current row
                found = True
                if x.month >= 11:
                    if x.day >= 11:
                        messagebox.showinfo("Invalid","Coupon expired")
                elif row[2] == "C":
                    messagebox.showinfo("Invalid", "Code Already in Use")
                elif row[2] == "NC":
                    row[2] = updated_value
                    messagebox.showinfo("", "Code claimed Successfully")
                
    if not found :
        messagebox.showinfo("Invalid","Code Not found")

    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

    

root = tk.Tk()
root.title("QR Scanner App")
root.geometry("400x200")


qr_code = tk.Label(root, text="QR Code", font=("bold", 15))
qr_code.place(x=70, y=50)

entry_code = tk.Entry(root, width = 20)
entry_code.place(x=175, y=55)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

# Create the "Scan" button
check_button = tk.Button(button_frame, text="Check", command=scan_qr)
check_button.pack(side=tk.LEFT, padx=20)

# Create the "Exit" button
exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.RIGHT, padx=20)

# Run the main event loop
root.mainloop()

