from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_message = data.get("message", "").lower()

    if "hello" in user_message:
        return jsonify({"response": "Hello! How can I help you?"})
    elif "how are you" in user_message:
        return jsonify({"response": "I'm just a bot, but I'm functioning well. How can I assist you?"})
    else:
        return jsonify({"response": "I'm sorry, I don't understand that. Can you rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)
