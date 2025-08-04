from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Inicializa Flask
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Configuración de JWT (cambia la clave en producción)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Usuario de prueba para login básico
USER = {
    "email": "test@example.com",
    "password": "123456",
    "token": "fake-jwt-token-123"
}

# ---------------------------
# 🔐 API DE LOGIN (dummy)
# ---------------------------
@app.route('/api/v1/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Invalid request"}), 400
    
    if data['email'] == USER['email'] and data['password'] == USER['password']:
        return jsonify({"token": USER['token']}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# ---------------------------
# 🌐 RUTAS PARA PÁGINAS HTML
# ---------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/place')
def place():
    return render_template('place.html')

@app.route('/add-review')
def add_review():
    return render_template('add_review.html')

# ---------------------------
# MAIN
# ---------------------------

if __name__ == '__main__':
    app.run(debug=True)
