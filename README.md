# Episode 001 — CLI Chatbot with Memory

> takeaway: The model is an illusion you build in code, not something the model holds.

## The Problem / The Question
I wanted to understand how to actually build a chatbot that feels like a real conversation — not one that forgets everything after one message. The question I started with was how exactly does the model "know" what I said before, and what exactly do I send it to make that work?

## What I Built
A command-line chatbot that calls an LLM API and preserves the full conversation history across turns. You type a message, it responds, and every follow-up message is sent with the complete history so the model has full context. Built in Python, no framework yet, only raw API calls.

## What I Learned
- The chatbots memory is really just a list the code builds and sends it with every request. The model doesn't remember anything once the program exits. 
- We call it that the "model is stateless", which means every API request is independent
- Messages list is a list of dictionaries, each interaction with a "role" and "content" as keys.
- "max_tokens" caps how long the assistant reply can be (eg. output tokens)
- Always use a virtual environment for every Python project:  
Create it with `python3 -m venv venv`, activate it with `source venv/bin/activate`. 
It deactivates when you close the terminal, so you have to activate it again every new session.
- Environment variables are stored securely in .env and LOADED using the load_dotenv function
- The big picture: The user gets a welcome message at the screen, code runs forever until user decides to quit with keywords. Error handling wraps the API call and catches errors that happen during or after sending to the API

## How to Run
1. Clone the repo
```
   $ git clone https://github.com/zinebnadak/ep-001-cli-chatbot-memory
   $ cd ep-001-cli-chatbot-memory
```

3. Create and activate a virtual environment
```
   $ python3 -m venv venv
   $ source venv/bin/activate
```

5. Install dependencies
```
   $ pip install -r requirements.txt
```

6. Add your API key
```
$ cp .env.example .env
```
Open .env and replace with your actual Anthropic API key

8. Run
```
$ python src/main.py
```

## Tech Used
- `anthropic` — Python SDK for the Anthropic API (id: claude-haiku-4-5-20251001). Handles the HTTP, auth, and response parsing so the code stays focused on logic.
- `python-dotenv` — loads the API key from `.env` without hardcoding it anywhere.

## References
- [Anthropic — Claude API Docs/ Get started with Claude](https://platform.claude.com/docs/en/get-started)
- [Anthropic — Claude API Docs/ Using the Messages API guide](https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages)
- [Anthropic — Claude API Docs/ Messages API reference](https://docs.anthropic.com/en/api/messages)
- [gitignore.io](https://www.toptal.com/developers/gitignore)

---
*by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak?s=21) · [LinkedIn](https://www.linkedin.com/in/zinebnadak?utm_source=share_via&utm_content=profile&utm_medium=member_ios)*
