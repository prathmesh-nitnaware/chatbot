def get_response(user_input):
    user_input = user_input.lower()

    # Very basic rule-based logic
    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to PraWise AI. How can I assist you today?"
    elif "help" in user_input:
        return "I'm here to help! Ask me anything about productivity, study tips, or tech."
    elif "your name" in user_input:
        return "I'm PraWise AI, your smart assistant powered by Prathmesh."
    elif "bye" in user_input:
        return "Goodbye! Come back soon."
    else:
        return "Sorry, I'm just a demo version for now. But I'm learning fast!"
