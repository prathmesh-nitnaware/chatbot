from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', chat_history=[])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")

    if not user_input.strip():
        return jsonify({"response": "Please enter a message."})

    # Fallback local response
    if "hello" in user_input.lower():
        bot_response = "👋 Welcome to PraWise AI support!"
    elif "help" in user_input.lower():
        bot_response = "Sure, I'm here to help! Please ask your question."
    elif "features" in user_input.lower():
        bot_response = "I can assist with general queries, give information, and chat smartly!"
    else:
        bot_response = "Sorry, I'm not sure how to respond to that right now."

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
