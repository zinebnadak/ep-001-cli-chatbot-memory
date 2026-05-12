import os                                                                                          # to read the environment variable
from anthropic import Anthropic                                                                    # Anthropic class is the client that handle communication with the API
from dotenv import load_dotenv                                                                     # load_dotenv function reads .env file

load_dotenv()                                                                                      # read the .env file"
client = Anthropic()                                                                               # Creates an instant of the Antropic class - the API client



conversation_history = []                                                                          #memory, everythign here should be a dict with "role" and "content" keys
system_prompt = "You are a helpful loving asisstant"


print('Chatbot Ready. Type "exit" or "quit" to terminate')

while True:                                                                                        # should run forever until the user decides to terminate
    user_content = input("Type something: ")
    if user_content.lower() in ["quit", "exit"]:
        print("Goodbye")
        break

    conversation_history.append({"role" : "user", "content" : user_content})                        # append after so that "quit" or "exit" does not get appended
    
    message = client.messages.create(                                                               # API Call – after appending bcs API needs the user's message to be in the history before sending it
        model = "claude-haiku-4-5",
        max_tokens=200, 
        system = system_prompt,                                                                     # output tokens
        messages = conversation_history)
    print(f"Assistant: {message.content[0].text}")

    conversation_history.append({"role" : "assistant", "content" : message.content[0].text})        # "Message" is an object with attributes, use dot notation to access them 
    
print(conversation_history)