from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# User for testing
USER = {
    "email": "test@example.com",
    "password": "123456",
    "token": "fake-jwt-token-123"
}

@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Invalid request"}), 400
    
    if data['email'] == USER['email'] and data['password'] == USER['password']:
        return jsonify({"token": USER['token']}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
if __name__ == '__main__':
    app.run(debug=True)
