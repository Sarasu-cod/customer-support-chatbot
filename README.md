# Customer Support Chatbot
A simple AI-powered chatbot for customer support, built using:
- Python (NLP-based intent matching)
- Flask for the web interface
- Dialogflow for advanced NLP comparison

## Features
- Natural Language Processing (NLP)
- Basic intent-response handling in Python
- HTML frontend for chat interaction
- Option to switch to Dialogflow for better NLP
- Easy to extend and customize

## Project Structure
```
customer-support-bot/
├── app.py                 # Flask web server
├── chatbot.py             # Chatbot logic (NLP-based)
├── templates/
│   └── index.html         # Chat UI
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-support-bot.git
   cd customer-support-bot
   ```
2. Install dependencies
3. Run the app:
   ```bash
   python app.py
   ```

4. Open in browser:
   ```
   http://localhost:5000
   ```

## 💬 How It Works

- User types a query in the UI
- Python (chatbot.py) processes it using keyword/NLP
- Response is sent back via Flask to the frontend
- You can switch to Dialogflow for better NLP

## 🔗 Dialogflow Setup (Optional)

1. Go to [Dialogflow Console](https://dialogflow.cloud.google.com/)
2. Create a new agent named `Customer_Support_Chatbot`
3. Add intents and responses

## 🧪 Example Questions

- “Where is my order?”
- “I forgot my password”
- “Can I cancel my subscription?”
- “Talk to a human agent”

## References
1. Natural Language Toolkit (NLTK) -  https://www.nltk.org/
   Used for basic NLP tasks such as tokenization and intent matching.
2. Flask Documentation -  https://flask.palletsprojects.com/
   Used to build the backend API and serve the frontend interface.
3. Dialogflow Documentation -  https://cloud.google.com/dialogflow/docs
   Used for building the cloud-based version of the chatbot.
4. Tutorials and examples refernced:
   https://realpython.com/python-chat-bot/
   https://www.geeksforgeeks.org/ml-building-a-chatbot-using-python/
