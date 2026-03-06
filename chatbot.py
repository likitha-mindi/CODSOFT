# Rule-Based Chatbot for CodSoft Task 1

print("Hello! I am a simple chatbot.")
print("Type 'bye' to end the conversation.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: I am a rule-based chatbot created for CodSoft internship.")

    elif user == "who created you":
        print("Bot: I was created by Likitha.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
