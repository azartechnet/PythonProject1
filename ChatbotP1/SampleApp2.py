from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#import chatterbot

chatbot = ChatBot("EcommerceBot")
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")
custom_conversations = [
    "What products do you offer?",
    "How can I track my order?",
    "Do you have any discounts or promotions?",
    "Tell me more about product X.",
    # Add more custom conversations relevant to your E-commerce platform
]

trainer.train(custom_conversations)
# Sample product data (you can replace this with actual product data from your E-commerce platform)
products = {
    "product1": {
        "name": "Product 1",
        "description": "This is a sample product.",
        "price": "$10.99",
        "available": True,
    },
    "product2": {
        "name": "Product 2",
        "description": "Another sample product.",
        "price": "$19.99",
        "available": False,
    },
    # Add more products
}

# Function to fetch product details
def get_product_details(product_name):
    product = products.get(product_name.lower())
    if product:
        response = f"{product['name']} - {product['description']}\nPrice: {product['price']}"
        if product['available']:
            response += "\nAvailable: Yes"
        else:
            response += "\nAvailable: No"
    else:
        response = "Sorry, I couldn't find information about that product."
    return response
def process_user_input(user_input):
    response = chatbot.get_response(user_input)
    if "product" in user_input.lower():
        product_name = user_input.replace("product", "").strip()
        response = get_product_details(product_name)
    return response.text

# Sample interaction loop
print("EcommerceBot: Hi! I'm your E-commerce assistant. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("EcommerceBot: Goodbye!")
        break

    response = process_user_input(user_input)
    print("EcommerceBot:", response)

