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
