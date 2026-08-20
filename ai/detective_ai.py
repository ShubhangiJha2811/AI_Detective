import os

from dotenv import load_dotenv

from google import genai


# Load .env
load_dotenv()


API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


# Create Gemini client
client = None

if API_KEY:

    try:

        client = genai.Client(
            api_key=API_KEY
        )

    except Exception:

        client = None


def ask_ai(prompt):

    if client is None:

        return (
            "⚠️ Gemini API is not configured.\n\n"
            "Please check your .env file."
        )

    try:

        response = client.models.generate_content(

            model=MODEL,

            contents=prompt
        )

        if response.text:

            return response.text

        return "The AI did not return a response."

    except Exception as error:

        error_message = str(error).lower()

        if "429" in error_message:

            return (
                "⚠️ Gemini API quota has been reached.\n\n"
                "The game can continue using "
                "the available clues."
            )

        if "503" in error_message:

            return (
                "⚠️ Gemini is temporarily busy.\n\n"
                "Please try again in a moment."
            )

        return (
            "⚠️ AI service is currently unavailable."
        )


def analyze_case(
    case,
    suspects,
    clues,
    interrogations
):

    suspects_text = "\n".join(

        [
            (
                f"- {s['name']} | "
                f"Occupation: {s['occupation']} | "
                f"Alibi: {s['alibi']} | "
                f"Motive: {s['motive']}"
            )

            for s in suspects
        ]
    )


    clues_text = "\n".join(

        [
            (
                f"- {c['name']}: "
                f"{c['description']}"
            )

            for c in clues
        ]
    )


    interrogation_text = "\n".join(

        [
            (
                f"- {i['suspect']}: "
                f"{i['question']} "
                f"-> {i['answer']}"
            )

            for i in interrogations
        ]
    )


    prompt = f"""
You are an expert detective assistant.

You are helping a player solve a mystery.

CASE:
{case['description']}

LOCATION:
{case['location']}

TIME:
{case['time']}

SUSPECTS:
{suspects_text}

CLUES:
{clues_text}

INTERROGATIONS:
{interrogation_text}

Analyze the investigation.

Do NOT directly reveal the culprit.

Give:

1. Strongest evidence
2. Suspicious behavior
3. Contradictions
4. Which suspect deserves more investigation
5. One recommended next question

Keep the response concise.
"""


    return ask_ai(prompt)


def generate_hint(
    case,
    suspects,
    clues
):

    prompt = f"""
You are a detective game assistant.

CASE:
{case['title']}

DESCRIPTION:
{case['description']}

SUSPECTS:
{[s['name'] for s in suspects]}

CLUES:
{[c['name'] for c in clues]}

Give the player ONE subtle hint.

Do NOT reveal the culprit.

Encourage the player to examine evidence.
"""


    return ask_ai(prompt)