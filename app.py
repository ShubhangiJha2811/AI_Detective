import streamlit as st


# Game data
from game.cases import CASES
from game.suspects import SUSPECTS
from game.clues import CLUES


# Game logic
from game.game_logic import (
    create_game_state,
    add_interrogation,
    add_clue,
    finish_game,
    get_remaining_turns
)


# Scoring
from game.scoring import (
    calculate_score,
    get_rank,
    compare_with_ai
)


# AI
from ai.interrogation import (
    interrogate_suspect
)

from ai.detective_ai import (
    analyze_case,
    generate_hint
)

from ai.judge import (
    judge_case,
    reveal_solution
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(

    page_title="AI Detective",

    page_icon="🕵️",

    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #080b14;
}

.detective-title {

    font-size: 48px;

    font-weight: 800;

    text-align: center;

    color: #8b5cf6;

    margin-bottom: 5px;
}

.subtitle {

    text-align: center;

    color: #94a3b8;

    font-size: 18px;

    margin-bottom: 30px;
}

.case-card {

    padding: 25px;

    border-radius: 15px;

    background-color: #111827;

    border: 1px solid #374151;

    margin-bottom: 20px;
}

.ai-box {

    padding: 20px;

    border-radius: 15px;

    background-color: #111827;

    border: 1px solid #8b5cf6;
}

.clue-card {

    padding: 15px;

    border-radius: 12px;

    background-color: #111827;

    border-left: 4px solid #8b5cf6;

    margin-bottom: 12px;
}

</style>
""",
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE
# ==================================================

if "game" not in st.session_state:

    st.session_state.game = None


if "case_name" not in st.session_state:

    st.session_state.case_name = None


if "ai_analysis" not in st.session_state:

    st.session_state.ai_analysis = None


if "hint" not in st.session_state:

    st.session_state.hint = None


if "last_answer" not in st.session_state:

    st.session_state.last_answer = None


if "final_result" not in st.session_state:

    st.session_state.final_result = None


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="detective-title">'
    '🕵️ AI DETECTIVE'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">'
    'Human vs Machine — Can You Solve the Mystery?'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("🎮 Game Control")


    if st.button(
        "🔄 New Game",
        use_container_width=True
    ):

        st.session_state.game = None

        st.session_state.case_name = None

        st.session_state.ai_analysis = None

        st.session_state.hint = None

        st.session_state.last_answer = None

        st.session_state.final_result = None

        st.rerun()


    st.divider()


    st.subheader("📖 How To Play")

    st.write(
        """
        **1.** Select a case.

        **2.** Read the case.

        **3.** Study suspects.

        **4.** Investigate clues.

        **5.** Interrogate suspects.

        **6.** Ask the AI detective.

        **7.** Make your accusation.

        **8.** Beat the AI.
        """
    )


    st.divider()


    st.caption(
        "🤖 Powered by Gemini AI"
    )


# ==================================================
# CASE SELECTION
# ==================================================

if st.session_state.game is None:

    st.subheader("📂 Select Your Case")


    case_names = list(
        CASES.keys()
    )


    selected_case = st.selectbox(

        "Choose a mystery",

        case_names
    )


    case = CASES[selected_case]


    st.markdown(

        f"""
<div class="case-card">

<h2>🗂️ {case['title']}</h2>

<p>
<b>Difficulty:</b>
{case['difficulty']}
</p>

<p>
<b>Location:</b>
{case['location']}
</p>

<p>
<b>Victim:</b>
{case['victim']}
</p>

<p>
<b>Time:</b>
{case['time']}
</p>

</div>
""",

        unsafe_allow_html=True
    )


    st.write(
        case["description"]
    )


    if st.button(

        "🚨 START INVESTIGATION",

        type="primary",

        use_container_width=True
    ):

        st.session_state.game = (
            create_game_state(
                selected_case
            )
        )


        st.session_state.case_name = (
            selected_case
        )


        st.rerun()


    st.stop()


# ==================================================
# CURRENT GAME
# ==================================================

game = st.session_state.game

case_name = st.session_state.case_name

case = CASES[case_name]

suspects = SUSPECTS[case_name]

clues = CLUES[case_name]


# ==================================================
# GAME STATISTICS
# ==================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "⏳ Turns",
        f"{game['turn']}/{game['max_turns']}"
    )


with col2:

    st.metric(
        "⭐ Score",
        game["score"]
    )


with col3:

    st.metric(
        "🔎 Clues Found",
        len(game["found_clues"])
    )


with col4:

    st.metric(
        "💬 Questions",
        game["question_count"]
    )


st.progress(
    min(
        game["turn"] / game["max_turns"],
        1.0
    )
)


# ==================================================
# CASE
# ==================================================

st.header(
    f"📂 {case['title']}"
)


with st.expander(
    "📖 Case Details",
    expanded=True
):

    st.write(
        case["description"]
    )


# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3, tab4 = st.tabs(

    [
        "👥 Suspects",
        "🔎 Evidence",
        "🤖 AI Detective",
        "⚖️ Final Accusation"
    ]
)


# ==================================================
# SUSPECTS
# ==================================================

with tab1:

    st.subheader(
        "👥 Suspects"
    )


    for suspect in suspects:

        with st.expander(
            f"🧑 {suspect['name']}"
        ):

            st.write(
                f"**Age:** {suspect['age']}"
            )

            st.write(
                f"**Occupation:** "
                f"{suspect['occupation']}"
            )

            st.write(
                f"**Personality:** "
                f"{suspect['personality']}"
            )

            st.write(
                f"**Alibi:** "
                f"{suspect['alibi']}"
            )

            st.write(
                f"**Possible Motive:** "
                f"{suspect['motive']}"
            )


# ==================================================
# CLUES
# ==================================================

with tab2:

    st.subheader(
        "🔎 Evidence Board"
    )


    for clue in clues:

        if clue["id"] in game["found_clues"]:

            st.markdown(

                f"""
<div class="clue-card">

<h4>🔓 {clue['name']}</h4>

<p>{clue['description']}</p>

<b>Importance:</b>
{clue['importance']}

</div>
""",

                unsafe_allow_html=True
            )


        else:

            if st.button(

                f"🔍 Investigate {clue['name']}",

                key=f"clue_{clue['id']}"
            ):

                add_clue(
                    game,
                    clue["id"]
                )


                game["score"] += (
                    clue["points"]
                )


                st.rerun()


# ==================================================
# AI DETECTIVE
# ==================================================

with tab3:

    st.subheader(
        "🤖 AI Detective Assistant"
    )


    st.write(
        """
The AI can analyze the evidence and
help you decide what to investigate next.
"""
    )


    if st.button(
        "🧠 Analyze Evidence",
        use_container_width=True
    ):

        with st.spinner(
            "AI is analyzing the case..."
        ):

            st.session_state.ai_analysis = (
                analyze_case(
                    case,
                    suspects,
                    clues,
                    game["interrogations"]
                )
            )


    if st.session_state.ai_analysis:

        st.markdown(
            '<div class="ai-box">',
            unsafe_allow_html=True
        )


        st.markdown(
            st.session_state.ai_analysis
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    st.divider()


    if st.button(
        "💡 Give Me A Hint",
        use_container_width=True
    ):

        with st.spinner(
            "AI is thinking..."
        ):

            st.session_state.hint = (
                generate_hint(
                    case,
                    suspects,
                    clues
                )
            )


    if st.session_state.hint:

        st.info(
            st.session_state.hint
        )


# ==================================================
# INTERROGATION
# ==================================================

st.divider()

st.header(
    "🎤 Interrogation Room"
)


suspect_names = [

    suspect["name"]

    for suspect in suspects
]


selected_suspect = st.selectbox(

    "Choose a suspect",

    suspect_names
)


question = st.text_area(

    "Ask your question",

    placeholder=(
        "Example: Where were you at 11:45 PM?"
    ),

    height=100
)


remaining_turns = (
    get_remaining_turns(game)
)


st.caption(
    f"Investigation turns remaining: "
    f"{remaining_turns}"
)


if st.button(
    "🎤 INTERROGATE",
    type="primary"
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )


    elif remaining_turns <= 0:

        st.error(
            "You have used all your turns."
        )


    else:

        suspect_data = next(

            suspect

            for suspect in suspects

            if suspect["name"]
            == selected_suspect
        )


        with st.spinner(
            f"{selected_suspect} is answering..."
        ):

            answer = interrogate_suspect(

                case,

                suspect_data,

                question,

                game["interrogations"]
            )


        add_interrogation(

            game,

            selected_suspect,

            question,

            answer
        )


        st.session_state.last_answer = {

            "suspect": selected_suspect,

            "question": question,

            "answer": answer
        }


        st.rerun()


# ==================================================
# LAST ANSWER
# ==================================================

if st.session_state.last_answer:

    answer = (
        st.session_state.last_answer
    )


    st.subheader(
        f"🗣️ {answer['suspect']}"
    )


    st.chat_message(
        "user"
    ).write(
        answer["question"]
    )


    st.chat_message(
        "assistant"
    ).write(
        answer["answer"]
    )


# ==================================================
# INTERROGATION HISTORY
# ==================================================

if game["interrogations"]:

    with st.expander(
        "📜 Interrogation History"
    ):

        for item in game["interrogations"]:

            st.markdown(
                f"""
**🧑 {item['suspect']}**

**Detective:**
{item['question']}

**Suspect:**
{item['answer']}

---
"""
            )


# ==================================================
# FINAL ACCUSATION
# ==================================================

with tab4:

    st.subheader(
        "⚖️ Make Your Final Accusation"
    )


    st.warning(
        "Submitting your accusation "
        "will end the investigation."
    )


    accusation = st.selectbox(

        "Who is the culprit?",

        suspect_names,

        key="final_suspect"
    )


    reasoning = st.text_area(

        "Explain your reasoning",

        placeholder=(
            "Explain which clues and "
            "interrogation responses "
            "led you to your conclusion..."
        ),

        height=150
    )


    if st.button(

        "⚖️ SUBMIT ACCUSATION",

        type="primary",

        use_container_width=True
    ):

        if not reasoning.strip():

            st.warning(
                "Please explain your reasoning."
            )


        else:

            with st.spinner(
                "AI Judge is reviewing your investigation..."
            ):

                judge_result = judge_case(

                    case,

                    accusation,

                    reasoning,

                    clues,

                    game["interrogations"]
                )


            correct = (

                accusation
                == case["solution"]["culprit"]
            )


            final_score = calculate_score(

                case_name,

                accusation,

                case["solution"]["culprit"],

                game["found_clues"],

                len(clues),

                game["question_count"]
            )


            game["score"] = final_score


            finish_game(

                game,

                accusation
            )


            st.session_state.final_result = {

                "judge": judge_result,

                "correct": correct,

                "score": final_score
            }


            st.rerun()


# ==================================================
# FINAL RESULT
# ==================================================

if st.session_state.final_result:

    result = (
        st.session_state.final_result
    )


    st.divider()


    st.header(
        "🏁 Investigation Complete"
    )


    if result["correct"]:

        st.success(
            "🎉 CORRECT! "
            "You identified the culprit!"
        )

    else:

        st.error(
            "❌ INCORRECT! "
            "The culprit escaped your investigation."
        )


    st.metric(
        "Final Score",
        f"{result['score']}/100"
    )


    st.subheader(
        get_rank(
            result["score"]
        )
    )


    st.markdown(
        result["judge"]
    )


    st.divider()


    st.subheader(
        "🤖 HUMAN VS AI"
    )


    comparison = compare_with_ai(

        result["score"]
    )


    if comparison["result"] == "human":

        st.success(
            comparison["message"]
        )

    elif comparison["result"] == "ai":

        st.error(
            comparison["message"]
        )

    else:

        st.info(
            comparison["message"]
        )


    st.divider()


    st.subheader(
        "🔐 Actual Solution"
    )


    st.markdown(
        reveal_solution(case)
    )