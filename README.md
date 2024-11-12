# Email Phishing Detection Tool

A Python-based tool for detecting phishing content in emails. This tool provides a simple graphical user interface (GUI) to analyze email text for common phishing phrases, helping users identify potentially malicious emails.

## Features
- **Easy-to-Use Interface**: A clean, simple GUI for pasting email content and receiving instant feedback.
- **Real-Time Detection**: Scans email content for phishing phrases and provides results immediately.
- **Scrollable Input Box**: Allows for easy entry of large email content.

## Requirements
- Python 3
- `nltk` and `tkinter` libraries

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

