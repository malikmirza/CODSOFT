def simple_chatbot(user_input):
# Normalize user input to lower case for easier matching
user_input = user_input.lower()

# Define responses based on user input
if "hello" in user_input or "hi" in user_input:
return "Hello! How can I assist you today?"
elif "how are you" in user_input :
end
"I'm just a computer program, but thanks for asking! How can I help you?"
elif "what is your name" in user_input:
return "I am a simple chatbot created to assist you."
elif "help" in user_input:
return "Sure! What do you need"?
elif "bye" in user_input or "goodbye" in user_input:
return "Goodbye! Have a great day!"
else:
return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the user
def chat():
print("Welcome to the chatbot! Type 'bye' to exit.")
while True:
user_input = input("You: ")
if user_input.lower() in ["bye", "goodbye"]:
print("Chatbot: Goodbye! Have a great day!")
break
response = simple_chatbot(user_input)
print("Chatbot:", response)