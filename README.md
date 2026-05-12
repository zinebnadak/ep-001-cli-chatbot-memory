# Episode 001 — CLI Chatbot with Memory

> takeaway: 

## The Problem / The Question
I wanted to understand how to actually build a chatbot that feels like a real conversation — not one that forgets everything after one message. The question I started with was how exactly does the model "know" what I said before, and what exactly do I send it to make that work?

## What I Built
A command-line chatbot that calls an LLM API and preserves the full conversation history across turns. You type a message, it responds, and every follow-up message is sent with the complete history so the model has full context. Built in Python, no framework yet, only raw API calls.

## What I Learned
- [Specific finding — not generic]
- [The thing that surprised me]
- [The assumption that broke]
- [The detail worth remembering]

## How to Run
Step-by-step instructions. 

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