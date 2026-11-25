# 🕵️ AI Detective

A quick mystery game: find the culprit before you run out of moves.

## How to play

1. Pick a case.
2. You have **6 moves**. Each move lets you:
   - 🔎 **Examine** one piece of evidence, or
   - 🎤 **Ask** a suspect one question (*Where were you? / Why would you do it? / What are you hiding?*)
3. Find the suspect whose story doesn't match the evidence. Watch out for red herrings!
4. 👉 **Accuse** the culprit. You get 2 tries.

Earn up to ⭐⭐⭐:
- ⭐ Solve the case
- ⭐ No wrong accusations
- ⭐ Finish with 2+ moves left over

## AI feature (optional)

The game works without an API key. With a Gemini key, you can also type
your own questions, and the suspects answer in character (each costs 1 move).

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

## Run

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```
app.py               # The whole game screen
game/cases.py        # Cases, evidence, suspects and their answers
ai/detective_ai.py   # Gemini client
ai/interrogation.py  # AI answers to free-text questions
.streamlit/config.toml
```

## Adding a case

Add an entry to `CASES` in `game/cases.py` with a story, 4 clues,
4 suspects (with answers to the 3 questions), the culprit, and a confession.
