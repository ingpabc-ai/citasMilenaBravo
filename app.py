from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Milena Bravo está en línea 🚀"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Aquí procesas los mensajes que lleguen de WhatsApp / API
    print("Mensaje recibido:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
