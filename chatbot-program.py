import re

def simple_chatbot(user_input):
    # Predefined responses based on user input patterns
    responses = {}

    responses[r'.*hello.*'] = 'Hello! How can I help you?'
    responses[r'.*how are you.*'] = 'I am just a computer program, but thanks for asking!'
    responses[r'.*your name.*'] = 'I am a simple chatbot.'
    responses[r'.*help.*'] = 'I can assist you with basic questions. Just ask!'
    responses[r'.*who made you.*'] = 'I was created by Kaitlyn Jorns for her AI class.'
    responses[r'.*favorite color*'] = 'Pink.'
    responses[r'.*march madness winner.*'] = 'Probably Duke...'
    responses[r'.*marvel.*'] = 'My favorite Marvel character is Wanda Maximoff, the Scarlet Witch.'
    responses[r'.*star wars.*'] = 'My favorite Star Wars character is Anakin Skywalker.'

    # Iterate through predefined responses and find a match
    for pattern, response in responses.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return response

    # Default response for unrecognized input
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop for user interaction
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Get chatbot response
    chatbot_response = simple_chatbot(user_input)
    
    # Display chatbot response
    print("Chatbot:", chatbot_response)