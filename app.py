from flask import Flask, render_template, request, jsonify
from chatbot1 import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Invalid input. Please ask a question."})
    
    chatbot_response = get_response(user_message)
    return jsonify({"response": chatbot_response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Set the desired port here (e.g., 5001)
