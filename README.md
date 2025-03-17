# Track-Them

## Description  
Track-Them is a Python-based missing persons tracking system that helps in reporting, tracking, and updating the status of missing individuals. The system features OTP-based status updates, QR code generation, and Google Maps integration for last-seen locations.

## Features  
-  **Report Missing Person**: Collects details like name, age, gender, contact, last seen location, date, and time.  
-  **Email Alerts**: Sends an OTP to verify changes in missing status.  
-  **Search for Missing Persons**: Allows searching and displays information along with their photo.  
-  **View Last Seen Location**: Opens the last seen location in Google Maps.  
-  **Update Status**: Changes the status to "Found" or "Missing" after OTP verification.  
-  **QR Code Generation**: Creates a QR code containing details for quick reference.  
- 📂 **File Storage**: Saves missing persons' data in text files for easy retrieval.  

## Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/priyanshi496/Track-Them.git
2. pip install qrcode[pil] yagmail pillow
3. python track_them.py
## Dependencies
Python 3.x
qrcode for QR code generation
yagmail for sending emails
Pillow for handling images
webbrowser for Google Maps integration
## Usage
1. Run the script and follow the on-screen instructions.
2. To report a missing person, enter their details including an image.
3. An email alert will be sent to the authorities.
4. Search and update missing persons’ statuses as needed.
5. Generate QR codes and view last-seen locations on Google Maps.

   
