# 🕵️ AI Detective — Human vs Machine

AI Detective is an interactive mystery-solving game powered by AI.

The player investigates mysterious cases, discovers clues,
interrogates suspects and finally identifies the culprit.

## Features

- 🕵️ Detective cases
- 👥 Multiple suspects
- 🔎 Evidence investigation
- 🎤 AI-powered interrogation
- 🤖 AI Detective Assistant
- 💡 AI hints
- ⚖️ AI Judge
- ⭐ Scoring system
- 🏆 Detective rankings
- 🤖 Human vs AI comparison
- 🎮 Streamlit interface

## Technologies

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Project Structure

AI_Detective/

├── ai/

│   ├── __init__.py

│   ├── detective_ai.py

│   ├── interrogation.py

│   └── judge.py

├── assets/

│   └── game/

├── game/

│   ├── __init__.py

│   ├── cases.py

│   ├── clues.py

│   ├── game_logic.py

│   ├── scoring.py

│   └── suspects.py

├── .env

├── app.py

├── README.md

└── requirements.txt

## Installation

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

GEMINI_MODEL=gemini-2.5-flash

## Run

Run the application using:

streamlit run app.py

## Game Flow

Select Case
↓
Read Case
↓
Study Suspects
↓
Investigate Clues
↓
Interrogate Suspects
↓
Ask AI Detective
↓
Make Accusation
↓
AI Judge
↓
Calculate Score
↓
Human vs AI

## Future Features

- Character images
- Case background images
- Sound effects
- Background music
- Timer
- Difficulty levels
- More cases
- Leaderboard
- Multiplayer mode
- AI-generated cases
- Voice interrogation