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
