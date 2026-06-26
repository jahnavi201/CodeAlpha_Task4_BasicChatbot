def chatbot():
    print("===================================")
    print("      🤖 Basic Python Chatbot")
    print("===================================")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How are you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print("Bot: That's great to hear!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python for the CodeAlpha Internship.")

        elif user == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Start the chatbot
chatbot()