import re
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Define phishing keywords
phishing_keywords = [
    "verify your account", "click here", "urgent action required",
    "suspend your account", "update your information", "login to your account",
    "verify immediately", "account compromised"
]

# Function to detect phishing
def detect_phishing(email_text):
    email_text = email_text.lower()
    for keyword in phishing_keywords:
        if keyword in email_text:
            return "Phishing Alert: Suspicious content detected!"
    return "Legitimate: No phishing content detected."

# Tkinter UI setup
def check_email():
    email_text = email_entry.get("1.0", "end-1c")
    result = detect_phishing(email_text)
    messagebox.showinfo("Detection Result", result)

# Initialize the main window
root = tk.Tk()
root.title("Email Phishing Detection Tool")
root.geometry("500x400")
root.config(bg="#f2f2f2")

# Header
header = tk.Label(root, text="Email Phishing Detection Tool", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
header.pack(fill=tk.X)

# Email input label
tk.Label(root, text="Enter Email Text Below:", font=("Helvetica", 12), bg="#f2f2f2").pack(pady=(20, 5))

# Email text input box (scrolled)
email_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 10))
email_entry.pack(padx=20, pady=10)

# Detect button
check_button = tk.Button(root, text="Check Email", command=check_email, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
check_button.pack(pady=10)

# Footer
footer = tk.Label(root, text="Phishing Detection Tool © 2024", font=("Helvetica", 10), bg="#f2f2f2", fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

# Run the app
root.mainloop()
