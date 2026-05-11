# Project Brief — Episode 001

## The goal

Build the simplest possible chatbot that maintains conversation history across turns. No framework. No UI. Just Python, an LLM API, and a loop that keeps the chat alive. The goal is not a polished product, but to understand the request-response cycle of an LLM API and the role of message history in creating continuity.

## Scope — in

- A Python CLI that runs a conversation loop until the user exits
- Sends the full message history with every request
- A system prompt that sets the assistant's behaviour
- Basic error handling (rate limits, API failures, empty responses)
- API key loaded from `.env`, it must never be hardcoded

## Scope — out

- No web UI or frontend of any kind
- No persistent storageh History lives in memory only, resets on exit
- No LangChain or other frameworks yet. Using only raw SDK calls.
- No streaming responses

## Key decisions to make during the build

- Choose either OpenAI SDK or Anthropic SDK
- How to structure the `messages` list. What a `system` role vs `user` vs `assistant` role actually means...
- Where to append the assistant's reply to the history after each turn
- What to do when the API returns an error — it should crash gracefully and handled

## The concept I am testing

"Memory" is an illusion created by the client. You send the full conversation history with every call, and the model reasons over all of it. This project is a direct demonstration of that mechanic.

## Done when

- Multi-turn conversation works and follow-up questions reference earlier answers
- Exits cleanly on `quit` or `exit` without a traceback
- README is written and all sections are filled
- Pushed to GitHub with meaningful commit history

---
*by [Zineb Nadak](https://github.com/zinebnadak) · [X](https://x.com/zinebnadak?s=21) · [LinkedIn](https://www.linkedin.com/in/zinebnadak?utm_source=share_via&utm_content=profile&utm_medium=member_ios)*