from flask import Flask, request, jsonify, render_template
from chatbot import get_intent

app = Flask(__name__)

responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You are welcome!",
    "order_status": "You can track your order using the track link sent to your email.",
    "refund": "To request a refund, please fill out the form on our support page.",
    "default": "Sorry, I didn't get that. Could you please rephrase?"
}

@app.route("/")
def index():
    print("serving index.html")
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input=request.json.get("message", "")
    try:
        intent = get_intent(user_input)
        response = responses.get(intent, responses["default"])
    except:
        response = responses["default"]
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)