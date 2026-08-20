from .detective_ai import ask_ai


def interrogate_suspect(
    case,
    suspect,
    question,
    previous_questions=None
):

    if previous_questions is None:

        previous_questions = []


    history = "\n".join(

        [
            (
                f"Question: {item['question']}\n"
                f"Answer: {item['answer']}"
            )

            for item in previous_questions
        ]
    )


    prompt = f"""
You are role-playing as a suspect
in an AI detective game.

CASE:
{case['description']}

SUSPECT:

Name:
{suspect['name']}

Age:
{suspect['age']}

Occupation:
{suspect['occupation']}

Personality:
{suspect['personality']}

Alibi:
{suspect['alibi']}

Possible Motive:
{suspect['motive']}

Secret:
{suspect['secret']}

PREVIOUS QUESTIONS:
{history}

PLAYER QUESTION:
{question}

RULES:

1. Stay completely in character.
2. Do not immediately confess.
3. Answer naturally.
4. Become nervous if the question is strong.
5. You can become defensive.
6. You can contradict yourself.
7. Do not reveal your secret too easily.
8. Do not mention AI.
9. Answer in 2 to 5 sentences.
10. Make the interrogation feel realistic.

Respond only as the suspect.
"""


    return ask_ai(prompt)