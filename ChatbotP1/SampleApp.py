import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you.",
    "what is your name": "I'm a chatbot, you can call me ChatGPT.",
    "bye": "Goodbye! Have a great day!"
}
def chatbot_response(user_input):
    # Tokenize user input
    words = word_tokenize(user_input)

    # Check if any word in user input is a key in the responses dictionary
    for word in words:
        if word.lower() in responses:
            return responses[word.lower()]

    # If no matching keyword found, use a generic response
    return "I'm sorry, I don't understand. Can you please rephrase?"
def main():
    print("Chatbot: Hi, I'm ChatGPT. How can I assist you today? (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
