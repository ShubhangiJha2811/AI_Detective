from .cases import CASES
from .suspects import SUSPECTS
from .clues import CLUES


def get_case(case_name):
    return CASES.get(case_name)


def get_suspects(case_name):
    return SUSPECTS.get(case_name, [])


def get_clues(case_name):
    return CLUES.get(case_name, [])


def create_game_state(case_name):

    return {
        "case": case_name,
        "turn": 0,
        "max_turns": 10,
        "score": 0,
        "question_count": 0,
        "interrogations": [],
        "found_clues": [],
        "final_answer": None,
        "game_over": False
    }


def add_interrogation(
    state,
    suspect,
    question,
    answer
):

    state["interrogations"].append({

        "suspect": suspect,

        "question": question,

        "answer": answer
    })

    state["question_count"] += 1

    state["turn"] += 1

    return state


def add_clue(state, clue_id):

    if clue_id not in state["found_clues"]:

        state["found_clues"].append(clue_id)

    return state


def get_remaining_turns(state):

    return max(
        0,
        state["max_turns"] - state["turn"]
    )


def is_game_over(state):

    return (
        state["turn"] >= state["max_turns"]
        or state["game_over"]
    )


def finish_game(
    state,
    final_answer
):

    state["final_answer"] = final_answer

    state["game_over"] = True

    return state