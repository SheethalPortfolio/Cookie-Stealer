Q2 – Cookie Stealer Instructions

1. Boot Kali and Meta2 VMs on same NAT network.

2. On Kali:
   cd ~/myproject
   source venv/bin/activate
   python3 stealer.py

3. In Kali browser:
   - Visit http://10.0.2.4/dvwa
   - Login: admin / password
   - Set DVWA security to "Medium"
   - Go to XSS (Reflected)
   - Paste the payload from xss_payload.txt and click Submit

4. The Flask server receives the cookie and saves it in cookies.txt

5. To verify, run:
   cd ~/myproject
   cat cookies.txt


In addition another method where the py and js.txt script changed name

Q2 – Cookie Stealer Instructions

1. Boot Kali and Meta2 VMs on the same NAT network.

2. On Kali:
   cd /home/sheethal/Documents/Q2
   python3.13 -m venv venv
   source venv/bin/activate
   pip install flask
   python3 cookie_server.py

3. Open Chromium/Firefox on Kali:
   chromium/Firefox 

   - Visit: http://10.0.2.4/dvwa
     (Replace with your actual Meta2 IP if different)

   - Login: admin / password
   - Go to: DVWA Security → Set to "Medium"
   - Go to: XSS (Reflected)
   - Paste the payload from cookie_stealer.js.txt and click Submit

4. The Flask server running on Kali receives the cookie from DVWA and appends it to a file named `cookies.txt`.

Note:
- 'cookies.txt' is automatically created by the Python code the first time a cookie is received.
- If you try to read it (using 'cat cookies.txt') before any cookie is received, the file may not exist yet.
- Optional: To avoid a "No such file or directory" error during testing, you may create an empty file using:
    touch cookies.txt


5. To verify the cookie has been received:
   - Open a second terminal on Kali
   - Run:
     cd /home/sheethal/Documents/Q2
     cat cookies.txt

   - You should see entries like:
     [2025-07-28 12:34:56] Cookie: PHPSESSID=abc123xyz

---

Troubleshooting:

- If nothing is received:
  - Double check the IP address in your payload inside 'cookie_stealer.js.txt' matches your Kali IP (use 'ifconfig').
  - Make sure Flask is running **before** you submit the XSS payload.
  - Use Chromium instead of Meta2’s browser — Meta2’s Firefox may block JavaScript silently.
