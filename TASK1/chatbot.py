def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "name" in user_input:
        return "I am a simple rule-based chatbot created to assist you."
    elif "help" in user_input:
        return "Sure! You can ask me about my features or just say 'goodbye' to exit."
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif "what can you do" in user_input:
        return ("I can chat with you, provide information, "
                "and answer basic questions. Just ask!")
    elif "joke" in user_input:
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif "weather" in user_input:
        return "I can't check the weather right now, but it's always nice to stay indoors!"
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "tell me a fact" in user_input:
        return "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible."
    else:
        return "I'm sorry, I don't understand that. You can ask me 'help' for guidance."

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
