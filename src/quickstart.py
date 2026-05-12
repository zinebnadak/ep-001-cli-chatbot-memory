#testing Anthropics quickstart to confirm the API key works 


import anthropic
from dotenv import load_dotenv  #added

load_dotenv()                   #added
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)
print(message.content[0].text)