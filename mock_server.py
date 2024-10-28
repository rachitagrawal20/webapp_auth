from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
import os
import requests

# Initialize Flask app and auth
app = Flask(__name__)
auth = HTTPBasicAuth()

# Authentication details (username: user, password: passwd)
users = {
    "user": "passwd"
}

@auth.get_password
def get_pw(username):
    return users.get(username)

# Route for handling XML response
@app.route('/mock-endpoint', methods=['GET'])
@auth.login_required
def mock_endpoint():

    print("Received request:")
    url = 'https://xmlfeed-2.free.beeceptor.com/feed'# Optional: print XML for debug
    feed = requests.get(url, timeout=50)

    # Define a sample XML response
    response_xml = """<?xml version="1.0"?>
    <response>
        <status>Success</status>
        <message>Hello, this is a mock XML response!</message>
    </response>"""

    # Return response with XML content type
    return Response(feed.content, mimetype='application/xml')

# Run the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
