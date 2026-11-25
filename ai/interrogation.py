from .detective_ai import ask_ai


def interrogate_suspect(case, suspect, question):
    """Let the AI answer a free-text question in character."""

    guilty = suspect["name"] == case["culprit"]

    known_answers = "\n".join(
        f"- {answer}" for answer in suspect["answers"].values()
    )

    if guilty:
        role_rule = (
            "You ARE the culprit. Never confess, but stay consistent with "
            "the statements below and let one small nervous slip show."
        )
    else:
        role_rule = (
            "You are INNOCENT. Be honest, but you may be defensive "
            "about your own small secret."
        )

    prompt = f"""
You are role-playing a suspect in a detective game.

CASE: {case['story']}
TRUTH (never state it directly): the culprit is {case['culprit']}.

YOU ARE: {suspect['name']}, {suspect['role']}.
PERSONALITY: {suspect['personality']}
{role_rule}

THINGS YOU HAVE ALREADY SAID:
{known_answers}

DETECTIVE ASKS: {question}

Answer in character in 1 to 3 short sentences. Do not mention AI.
"""

    return ask_ai(prompt)
