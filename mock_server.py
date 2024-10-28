from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
import os

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
@app.route('/mock-endpoint', methods=['POST'])
@auth.login_required
def mock_endpoint():
    # Check if request content is XML
    if request.content_type != 'application/xml':
        return Response("Invalid Content-Type", status=400)

    # Parse incoming XML (if needed)
    incoming_xml = request.data.decode('utf-8')
    print("Received XML:", incoming_xml)  # Optional: print XML for debug

    # Define a sample XML response
    response_xml = """<?xml version="1.0"?>
    <response>
        <status>Success</status>
        <message>Hello, this is a mock XML response!</message>
    </response>"""

    # Return response with XML content type
    return Response(response_xml, mimetype='application/xml')

# Run the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
