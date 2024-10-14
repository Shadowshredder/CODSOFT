# Simple Rule-Based Chatbot

This project is a basic **rule-based chatbot** that responds to user inputs using predefined rules. It is a simple way to understand how chatbots can be developed without complex natural language processing models. The chatbot is built using basic **if-else statements** and **pattern matching techniques** to identify user queries and respond with appropriate, predefined answers.

## Project Description

The chatbot was developed to demonstrate a fundamental approach to **Natural Language Processing (NLP)** and conversation flow. By relying on a set of predefined rules, this chatbot can handle basic interactions with users. It recognizes keywords or patterns in the input text and responds accordingly. The main goal is to showcase how basic logic and control structures can be used to simulate a conversation.

### Features

- **Rule-Based Responses**: The chatbot uses simple rules to respond to specific user inputs. These rules are based on common greetings and questions.
- **Pattern Matching**: The chatbot matches parts of the user's input (e.g., keywords like "hello," "bye," or "how are you") to generate appropriate responses.
- **Basic Conversation Flow**: The chatbot engages in simple, predefined conversations to show the basic mechanics of interacting with a user.
- **Case-Insensitive Matching**: It converts the user’s input to lowercase to ensure case-insensitivity in matching.

### How It Works

The chatbot identifies keywords from the user’s input using basic if-else statements. For example:
- If the user says **“hello”**, the chatbot responds with a greeting.
- If the user asks **“how are you?”**, the chatbot gives a response about its own status.
- When the user says **“bye”**, the chatbot exits the conversation.

Here is a breakdown of how the chatbot processes user inputs:

1. The user input is captured and converted to lowercase for easier pattern matching.
2. The chatbot checks the input for predefined keywords or phrases.
3. Based on the keyword, the chatbot provides a predefined response.
4. The conversation continues until the user inputs "bye," which ends the chat session.

### Example Interaction
Chatbot: Hello! Type 'bye' to exit. You: Hello Chatbot: Hi there! How can I assist you today? You: How are you? Chatbot: I'm just a bot, but I'm doing great! How about you? You: What is your name? Chatbot: I'm your friendly rule-based chatbot. You: Bye Chatbot: Goodbye! Have a great day!
