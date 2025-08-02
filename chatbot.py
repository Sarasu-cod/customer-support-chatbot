from flask import Flask, request, jsonify
import pickle
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

app = Flask(__name__)

with open('intent_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You are welcome!",
    "order_status": "You can track your order using the track link sent to your email.",
    "refund": "To request a refund, please fill out the form on our support page.",
    "default": "Sorry, I didn't get that. Could you please rephrase?"
}

def get_intent(text):
    tokens = word_tokenize(text.lower())
    text_processed = ' '.join(tokens)
    X = vectorizer.transform([text_processed])
    intent = model.predict(X)[0]
    return intent

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    try:
        intent = get_intent(user_input)
        response = responses.get(intent, responses["default"])
    except:
        response = responses["default"]
    return jsonify({"response":response})

if __name__ == '__main__':
    app.run(debug=True)