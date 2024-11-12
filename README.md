# Email Phishing Detection Tool

A Python-based tool for detecting phishing content in emails. This tool provides a simple graphical user interface (GUI) to analyze email text for common phishing phrases, helping users identify potentially malicious emails.

## Features
- **Easy-to-Use Interface**: A clean, simple GUI for pasting email content and receiving instant feedback.
- **Real-Time Detection**: Scans email content for phishing phrases and provides results immediately.
- **Scrollable Input Box**: Allows for easy entry of large email content.

## Requirements
- Python 3
- `nltk` and `tkinter` libraries

### Requirements File (`requirements.txt`)
The `requirements.txt` file should contain the following:

```
nltk
```

Note: `tkinter` is part of the standard library for Python, so it doesn't need to be installed separately through `pip`.

## Installation

1. Clone the project or download the files to your local machine.
2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the terminal and navigate to the project directory:

   ```bash
   cd phishing_detector
   ```

2. Run the Python script to launch the tool:

   ```bash
   python3 detect_phishing.py
   ```

3. In the window, paste or type the email text you want to check and press **Check Email**. The tool will display an alert indicating whether phishing content is detected.

### Example Usage

- **Sample Phishing Email**:
  ```
  Dear Customer,

  Your account has been compromised. Please verify your information immediately by clicking here.

  Sincerely, Customer Support
  ```

- **Expected Output**: Phishing Alert: Suspicious content detected!

## More Email Samples

### Phishing Emails
1. **Urgent Action Required**:
   ```
   Dear Customer,

   Your account has been suspended due to suspicious activity. Please verify your account information immediately by clicking the link below. Failure to do so will result in permanent suspension of your account.

   Click here to verify your account.
   
   Sincerely,
   Customer Support
   ```

2. **Account Compromised**:
   ```
   Hello,

   We noticed unusual activity in your account. To secure your account, please log in to verify your information. Follow the link below and update your security details.

   [Login to your account](#)

   Regards,
   Security Team
   ```

3. **Payment Needed**:
   ```
   Dear User,

   Your payment method was declined. Please update your billing information to avoid service interruption. Click the link below to update your information.

   Update Billing Information Now
   
   Best regards,
   Accounts Department
   ```

4. **Tax Refund Scam**:
   ```
   Dear Taxpayer,

   We have calculated that you are eligible for a tax refund of $500. To receive your refund, please provide your account information by clicking on the link below.

   Claim My Refund

   Thank you,
   The Tax Department
   ```

### Legitimate Emails
1. **Newsletter Update**:
   ```
   Hi there,

   Here is your weekly newsletter! We’ve got exciting updates on our new products and upcoming events. Thank you for being a part of our community.

   Best,
   The Newsletter Team
   ```

2. **Order Confirmation**:
   ```
   Hello,

   Thank you for your purchase! Your order #12345 has been confirmed and will be shipped soon. You can track your order status through your account.

   Best regards,
   Customer Service
   ```

3. **Account Welcome Email**:
   ```
   Hi [User's Name],

   Welcome to [Company Name]! We’re excited to have you on board. You can log in to your account to start exploring our services. If you have any questions, feel free to reach out.

   Best,
   Support Team
   ```

## File Structure

The project directory is organized as follows:

```
phishing_detector/
├── detect_phishing.py      # Main Python script for the phishing detection tool
├── requirements.txt        # List of required Python libraries
├── README.md               # Project documentation
└── LICENSE                 # MIT License for the project
```

## Customizing Detection Keywords

To add more phishing keywords, open `detect_phishing.py` and edit the `phishing_keywords` list with additional phrases.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

