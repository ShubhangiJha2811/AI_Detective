def calculate_score(
    case_name,
    selected_suspect,
    correct_suspect,
    clues_found,
    total_clues,
    questions_used
):
    """
    Calculate the player's final detective score.

    Maximum score = 100

    50 points -> Correct culprit
    30 points -> Evidence discovered
    20 points -> Efficient investigation
    """

    score = 0

    # -----------------------------------------
    # 1. Correct culprit = 50 points
    # -----------------------------------------

    if selected_suspect == correct_suspect:
        score += 50

    # -----------------------------------------
    # 2. Evidence = 30 points
    # -----------------------------------------

    if total_clues > 0:

        evidence_score = int(
            (len(clues_found) / total_clues) * 30
        )

        score += evidence_score

    # -----------------------------------------
    # 3. Investigation efficiency = 20 points
    # -----------------------------------------

    if questions_used <= 5:

        score += 20

    elif questions_used <= 8:

        score += 10

    # -----------------------------------------
    # Maximum score = 100
    # -----------------------------------------

    return min(score, 100)


def get_rank(score):
    """
    Convert score into detective rank.
    """

    if score >= 90:

        return "🏆 Master Detective"

    elif score >= 75:

        return "🥇 Expert Detective"

    elif score >= 60:

        return "🥈 Skilled Detective"

    elif score >= 40:

        return "🥉 Junior Detective"

    else:

        return "🔍 Rookie Detective"


def compare_with_ai(human_score):
    """
    Compare the player's score against
    the AI detective's benchmark score.
    """

    # Temporary AI benchmark.
    # We can later make this a real AI investigation.
    ai_score = 70

    if human_score > ai_score:

        return {
            "result": "human",
            "message": (
                "🎉 HUMAN WINS! "
                "You outsmarted the AI!"
            )
        }

    elif human_score < ai_score:

        return {
            "result": "ai",
            "message": (
                "🤖 AI WINS! "
                "The machine was better this time."
            )
        }

    else:

        return {
            "result": "tie",
            "message": "🤝 IT'S A DRAW!"
        }