# ContextForge

ContextForge is a small project-ops system that turns messy human input into persistent project state.

It is built for the OpenAI Discord Dev Challenge: **Build a System, Not a Prompt**.

## What it does

ContextForge accepts messy notes, Discord dumps, task fragments, and TSV project lists, then converts them into structured project state.

It can detect:

- project name
- area
- status
- priority
- mode
- next step
- blocker
- review cycle
- notes
- current state

The goal is to help manage too many parallel projects by converting chaotic input into a small actionable operating view.

## Why this is a system, not a prompt

ContextForge is not a chatbot.

It has:

- persistent state
- TSV import
- SQLite storage
- structured project records
- update logic
- blocker detection
- daily focus generation
- anti-overload rules

Instead of just answering a message, it updates a project state database and produces the next operational action.

## How it uses OpenAI APIs

ContextForge uses OpenAI structured outputs to convert messy natural language into validated project data.

Example input:

```text
need to fix the mower tractor first. just change the oil, don’t disassemble the whole thing yet. if it still fails, then inspect seals and magnets.
