import streamlit as st

from game.cases import CASES, QUESTIONS
from ai.detective_ai import client as ai_client
from ai.interrogation import interrogate_suspect


MAX_MOVES = 6
MAX_LIVES = 2


st.set_page_config(page_title="AI Detective", page_icon="🕵️", layout="wide")

st.markdown(
    """
<style>
.title {font-size: 46px; font-weight: 800; text-align: center; color: #a78bfa; margin-bottom: 0;}
.subtitle {text-align: center; color: #94a3b8; font-size: 18px; margin-bottom: 24px;}
.big {font-size: 22px; text-align: center;}
.quote {border-left: 3px solid #a78bfa; padding: 4px 12px; margin: 6px 0; color: #e2e8f0;}
</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# STATE
# ==================================================

def start_case(case_name):
    st.session_state.case_name = case_name
    st.session_state.moves = MAX_MOVES
    st.session_state.lives = MAX_LIVES
    st.session_state.seen_clues = set()
    st.session_state.answers = {}       # suspect name -> list of (question, answer)
    st.session_state.asked = set()      # (suspect name, question key)
    st.session_state.wrong = set()      # wrongly accused suspects
    st.session_state.message = None
    st.session_state.result = None      # None, "won" or "lost"


def go_home():
    st.session_state.case_name = None


def examine(index):
    if st.session_state.moves > 0:
        st.session_state.seen_clues.add(index)
        st.session_state.moves -= 1


def ask(suspect, key):
    if st.session_state.moves > 0:
        st.session_state.asked.add((suspect["name"], key))
        st.session_state.answers.setdefault(suspect["name"], []).append(
            (QUESTIONS[key], suspect["answers"][key])
        )
        st.session_state.moves -= 1


def accuse(name, case):
    if name == case["culprit"]:
        st.session_state.result = "won"
        return

    st.session_state.wrong.add(name)
    st.session_state.lives -= 1

    if st.session_state.lives <= 0:
        st.session_state.result = "lost"
    else:
        st.session_state.message = (
            f"❌ **{name}** has a solid alibi! You have one accusation left. "
            "Think carefully..."
        )


def stars():
    count = 1
    if not st.session_state.wrong:
        count += 1
    if st.session_state.moves >= 2:
        count += 1
    return count


if "case_name" not in st.session_state:
    go_home()


st.markdown('<div class="title">🕵️ AI DETECTIVE</div>', unsafe_allow_html=True)


# ==================================================
# HOME SCREEN
# ==================================================

if st.session_state.case_name is None:

    st.markdown(
        '<div class="subtitle">Find the culprit before you run out of moves.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="big">
🔎 Examine evidence &nbsp;·&nbsp; 🎤 Question suspects &nbsp;·&nbsp; 👉 Accuse the culprit
</div>
<p style="text-align:center;color:#94a3b8">
You only get <b>{MAX_MOVES} moves</b> and <b>{MAX_LIVES} accusations</b>.
Some clues are red herrings. Choose wisely!
</p>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    columns = st.columns(len(CASES))

    for column, (name, case) in zip(columns, CASES.items()):
        with column, st.container(border=True):
            st.markdown(f"<div style='font-size:56px;text-align:center'>{case['emoji']}</div>", unsafe_allow_html=True)
            st.subheader(name)
            st.caption(f"Difficulty: {case['difficulty']}")
            st.write(case["story"])
            st.button("▶ Play", key=f"play_{name}", type="primary",
                      width="stretch", on_click=start_case, args=(name,))

    st.stop()


# ==================================================
# GAME SCREEN
# ==================================================

case_name = st.session_state.case_name
case = CASES[case_name]
moves = st.session_state.moves
playing = st.session_state.result is None


# ---------- Header ----------

st.header(f"{case['emoji']} {case_name}")
st.info(case["story"])

status_left, status_right = st.columns(2)
status_left.markdown(
    f"### 🔦 Moves: {'🟣' * moves}{'⚫' * (MAX_MOVES - moves)}"
)
status_right.markdown(
    f"### Accusations: {'❤️' * st.session_state.lives}{'🖤' * (MAX_LIVES - st.session_state.lives)}"
)

if st.session_state.message and playing:
    st.warning(st.session_state.message)


# ==================================================
# RESULT
# ==================================================

if not playing:

    culprit = case["culprit"]

    with st.container(border=True):
        if st.session_state.result == "won":
            st.balloons()
            earned = stars()
            st.markdown(f"## 🎉 Case solved! It was **{culprit}**.")
            st.markdown(f"# {'⭐' * earned}{'☆' * (3 - earned)}")
            st.caption("⭐ Solved  ·  ⭐ No wrong accusations  ·  ⭐ 2+ moves left over")
        else:
            st.markdown(f"## 💨 The culprit escaped! It was **{culprit}**.")

        st.markdown(f"<div class='quote'>{case['confession']}</div>", unsafe_allow_html=True)

    names = list(CASES)
    next_case = names[(names.index(case_name) + 1) % len(names)]

    again, nxt, home = st.columns(3)
    again.button("🔁 Play again", width="stretch", on_click=start_case, args=(case_name,))
    nxt.button(f"➡️ Next: {next_case}", type="primary", width="stretch",
               on_click=start_case, args=(next_case,))
    home.button("🏠 All cases", width="stretch", on_click=go_home)

    # Show only the result: hide the evidence, suspects and accuse sections.
    st.stop()


# ==================================================
# EVIDENCE + SUSPECTS
# ==================================================

out_of_moves = moves <= 0 or not playing

if moves <= 0 and playing:
    st.error("⏰ Out of moves! Time to make your accusation below.")

evidence_col, suspects_col = st.columns([2, 3], gap="large")


with evidence_col:
    st.subheader("🔎 Evidence")
    st.caption("Each one costs 1 move.")

    for index, clue in enumerate(case["clues"]):
        with st.container(border=True):
            if index in st.session_state.seen_clues or not playing:
                st.markdown(f"**{clue['icon']} {clue['name']}**")
                st.markdown(clue["text"])
            else:
                st.markdown(f"**❓ {clue['name']}**")
                st.button("Examine", key=f"clue_{index}", width="stretch",
                          disabled=out_of_moves, on_click=examine, args=(index,))


with suspects_col:
    st.subheader("🎤 Suspects")
    st.caption("Each question costs 1 move. Watch for anything that doesn't match the evidence!")

    for suspect in case["suspects"]:
        name = suspect["name"]

        with st.container(border=True):
            label = f"#### {suspect['emoji']} {name}"
            if name in st.session_state.wrong:
                label += "  ❌"
            st.markdown(label)
            st.caption(suspect["role"])

            for question, answer in st.session_state.answers.get(name, []):
                st.markdown(
                    f"<div class='quote'><b>{question}</b><br>“{answer}”</div>",
                    unsafe_allow_html=True,
                )

            if playing:
                buttons = st.columns(len(QUESTIONS))
                for button, (key, question) in zip(buttons, QUESTIONS.items()):
                    button.button(
                        question,
                        key=f"ask_{name}_{key}",
                        width="stretch",
                        disabled=out_of_moves or (name, key) in st.session_state.asked,
                        on_click=ask,
                        args=(suspect, key),
                    )

                # Optional: free-text question answered by Gemini.
                if ai_client is not None and not out_of_moves:
                    with st.expander("✍️ Ask your own question (AI)"):
                        with st.form(key=f"form_{name}", clear_on_submit=True, border=False):
                            custom = st.text_input("Your question", key=f"text_{name}",
                                                   label_visibility="collapsed",
                                                   placeholder="e.g. Who else was near the lab?")
                            sent = st.form_submit_button("Ask (1 move)")

                        if sent and custom.strip():
                            with st.spinner(f"{name} is thinking..."):
                                reply = interrogate_suspect(case, suspect, custom.strip())
                            st.session_state.answers.setdefault(name, []).append(
                                (f"✍️ {custom.strip()}", reply)
                            )
                            st.session_state.moves -= 1
                            st.rerun()


# ==================================================
# ACCUSE
# ==================================================

if playing:
    st.divider()
    st.subheader("👉 Who did it?")
    st.caption("Accuse whenever you're ready. You don't need to use all your moves.")

    accuse_buttons = st.columns(len(case["suspects"]))

    for button, suspect in zip(accuse_buttons, case["suspects"]):
        name = suspect["name"]
        button.button(
            f"{suspect['emoji']} {name}",
            key=f"accuse_{name}",
            type="primary",
            width="stretch",
            disabled=name in st.session_state.wrong,
            on_click=accuse,
            args=(name, case),
        )


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.button("🏠 All cases", width="stretch", on_click=go_home)
    st.button("🔁 Restart case", width="stretch", on_click=start_case, args=(case_name,))
    st.divider()
    st.subheader("📖 How to play")
    st.write(
        "1. Examine evidence and question suspects (1 move each).\n"
        "2. Look for a story that doesn't match the evidence.\n"
        "3. Accuse the culprit. You have 2 tries."
    )
    if ai_client is None:
        st.caption("💡 Add a GEMINI_API_KEY to .env to ask suspects your own questions.")
