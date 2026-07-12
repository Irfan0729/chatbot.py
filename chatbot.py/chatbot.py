def start_chatbot():
    """
    This function runs the main loop of the chatbot.
    It takes user input and provides predefined responses.
    """
    print("🤖 Chatbot: Hello! I am your friendly Python Bot.")
    print("🤖 Chatbot: You can talk to me! (Type 'bye' to stop the conversation)")
    print("-" * 50)

    # The loop keeps the chatbot running until the user says 'bye'
    while True:
        # Get input from user, convert to lowercase, and remove extra spaces
        user_input = input("You: ").lower().strip()

        # Rule 1: Greeting
        if user_input == "hello" or user_input == "hi":
            print("🤖 Chatbot: Hi! How can I help you today?")

        # Rule 2: Asking about well-being
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! I'm just a program, but I'm feeling great!")

        # Rule 3: Asking for the bot's identity (Bonus)
        elif user_input == "what is your name":
            print("🤖 Chatbot: I am the CodeAlpha Basic Chatbot!")

        # Rule 4: Exit command
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a wonderful day! 👋")
            break  # This exits the while loop and ends the program

        # Fallback: If the user says something not predefined
        else:
            print("🤖 Chatbot: I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'.")

# This ensures the function only runs if the script is executed directly
if __name__ == "__main__":
    start_chatbot()
