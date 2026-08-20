from .detective_ai import ask_ai


def judge_case(
    case,
    selected_suspect,
    reasoning,
    clues,
    interrogations
):

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


    solution = case["solution"]


    prompt = f"""
You are the final judge
of an AI detective game.

CASE:
{case['description']}

ACTUAL CULPRIT:
{solution['culprit']}

ACTUAL MOTIVE:
{solution['reason']}

ACTUAL METHOD:
{solution['method']}

KEY EVIDENCE:
{solution['key_evidence']}

PLAYER ACCUSATION:
{selected_suspect}

PLAYER REASONING:
{reasoning}

CLUES:
{clues_text}

INTERROGATION HISTORY:
{interrogation_text}

Evaluate the player's investigation.

Return:

VERDICT: CORRECT or INCORRECT

SCORE: 0-100

FEEDBACK:

Explain:

- What the player did well
- What evidence they noticed
- What evidence they missed
- Whether their reasoning was convincing

Do not invent evidence.
"""


    return ask_ai(prompt)


def reveal_solution(case):

    solution = case["solution"]


    evidence = "\n".join(

        [
            f"- {item}"
            for item in solution["key_evidence"]
        ]
    )


    return f"""
### 🕵️ Case Solution

**Culprit:** {solution['culprit']}

**Motive:** {solution['reason']}

**Method:** {solution['method']}

### 🔎 Key Evidence

{evidence}
"""