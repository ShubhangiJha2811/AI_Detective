"""
All game content lives here.

Each case has:
  - a short story
  - 4 evidence cards (some are red herrings)
  - 4 suspects, each with 3 quick questions
  - the culprit and their confession
"""

# The same three quick questions are asked of every suspect.
QUESTIONS = {
    "where": "📍 Where were you?",
    "why": "🤔 Why would you do it?",
    "hiding": "🤫 What are you hiding?",
}


CASES = {

    "The Midnight Heist": {
        "emoji": "🧪",
        "difficulty": "Easy",
        "story": (
            "At **11:45 PM** the lights went out at TechNova Lab. "
            "When they came back, a top-secret **AI prototype** was gone. "
            "Only four people were in the building."
        ),
        "culprit": "Rohan Malhotra",
        "confession": (
            "\"Fine! I used my keycard during the blackout. A rival company "
            "offered me enough money to clear all my debts... I was never "
            "fixing my motorcycle.\""
        ),
        "clues": [
            {
                "icon": "🪪",
                "name": "Door Access Log",
                "text": "The **maintenance keycard** opened the lab door at 11:46 PM, one minute after the blackout.",
            },
            {
                "icon": "📹",
                "name": "Backup Camera",
                "text": "Grainy footage shows someone in an **orange maintenance jacket** near the lab.",
            },
            {
                "icon": "🅿️",
                "name": "Parking Gate Log",
                "text": "**No one** entered or used the parking lot between 11:00 PM and midnight.",
            },
            {
                "icon": "☕",
                "name": "Cafeteria Receipt",
                "text": "Priya bought a coffee in the cafeteria at **11:44 PM**.",
            },
        ],
        "suspects": [
            {
                "name": "Rohan Malhotra",
                "emoji": "🔧",
                "role": "Maintenance Engineer",
                "personality": "Nervous and defensive",
                "answers": {
                    "where": "Down in the parking lot, fixing my motorcycle. I didn't even notice the lights go out.",
                    "why": "Me? I just fix air conditioners. Okay, money is tight... but whose isn't?",
                    "hiding": "Nothing! My keycard has been in my pocket all night. Nobody else touched it. Why do you ask?",
                },
            },
            {
                "name": "Priya Nair",
                "emoji": "🔬",
                "role": "AI Researcher",
                "personality": "Calm and analytical",
                "answers": {
                    "where": "In the cafeteria getting coffee. Check the receipt if you like.",
                    "why": "Dr. Mehta took credit for my work, yes. But stealing it would ruin my own career.",
                    "hiding": "We had a loud argument this afternoon. That's all.",
                },
            },
            {
                "name": "Kabir Shah",
                "emoji": "👮",
                "role": "Security Officer",
                "personality": "Overconfident",
                "answers": {
                    "where": "At the security desk, watching the cameras.",
                    "why": "Steal from the place that pays me? I'd be the first one they'd suspect.",
                    "hiding": "...Fine. I switched off one camera to take a nap. But the backup camera was still recording!",
                },
            },
            {
                "name": "Meera Kapoor",
                "emoji": "💻",
                "role": "Software Engineer",
                "personality": "Friendly but anxious",
                "answers": {
                    "where": "I left at 11:20 PM. My badge-out record will show it.",
                    "why": "We were rivals, sure. But I already have a better job offer elsewhere.",
                    "hiding": "I copied some of my own code files this week. That's not a crime.",
                },
            },
        ],
    },


    "The Vanishing Necklace": {
        "emoji": "💎",
        "difficulty": "Medium",
        "story": (
            "During a private dinner at the Royal Heritage Hotel, "
            "Mrs. Kapoor's **diamond necklace** vanished from a locked "
            "display case at **9:30 PM**. Nobody saw a thing."
        ),
        "culprit": "Ananya Sharma",
        "confession": (
            "\"I had a copy of the key made two days ago. My business is "
            "drowning in debt, and that necklace was going to save it. "
            "I should never have worn this scarf.\""
        ),
        "clues": [
            {
                "icon": "🔑",
                "name": "Locksmith Receipt",
                "text": "A copy of the display key was made two days ago. The buyer paid cash and wore a **green silk scarf**.",
            },
            {
                "icon": "📸",
                "name": "Party Photos",
                "text": "Neha's photos show **Ananya's chair empty** at 9:28 PM.",
            },
            {
                "icon": "🗝️",
                "name": "Spare Key Box",
                "text": "The hotel's spare key is still **locked in the manager's box**, untouched.",
            },
            {
                "icon": "🧤",
                "name": "Display Case",
                "text": "Small fingerprints on the inside handle, with a faint smell of **rose perfume**.",
            },
        ],
        "suspects": [
            {
                "name": "Ananya Sharma",
                "emoji": "💼",
                "role": "Consultant, wearing a green silk scarf",
                "personality": "Charming but evasive",
                "answers": {
                    "where": "At the dinner table the whole evening. I never left my seat.",
                    "why": "Me? I'm doing perfectly well... although business has been a little slow lately.",
                    "hiding": "This scarf? It's a gift. I wear it everywhere. Why does everyone keep looking at it?",
                },
            },
            {
                "name": "Rahul Kapoor",
                "emoji": "😠",
                "role": "Mrs. Kapoor's nephew",
                "personality": "Hot-tempered",
                "answers": {
                    "where": "Out on the terrace arguing with my aunt's lawyer. Ask him.",
                    "why": "That necklace will be mine one day anyway. Why would I steal it?",
                    "hiding": "We fought about the inheritance. Everybody heard it. That's no secret.",
                },
            },
            {
                "name": "Neha Verma",
                "emoji": "📷",
                "role": "Fashion Designer",
                "personality": "Very talkative, loves rose perfume",
                "answers": {
                    "where": "Taking photos all night! Do you want to see them? I have hundreds.",
                    "why": "I adore that necklace. I wanted to sketch it, not steal it!",
                    "hiding": "I took a close-up photo of the display lock... for design inspiration!",
                },
            },
            {
                "name": "Amit Joshi",
                "emoji": "🏨",
                "role": "Hotel Manager",
                "personality": "Calm and professional",
                "answers": {
                    "where": "Supervising the kitchen. Twelve staff members saw me.",
                    "why": "My job and my reputation are worth far more than any necklace.",
                    "hiding": "I hold the only spare key. I checked it right away. It's still in my box.",
                },
            },
        ],
    },


    "The Deleted File": {
        "emoji": "💾",
        "difficulty": "Hard",
        "story": (
            "CyberCore was investigating a ransomware attack. At **2:17 AM** "
            "someone **deleted the entire investigation file** from the "
            "office server. Only four people had admin access."
        ),
        "culprit": "Vikram Singh",
        "confession": (
            "\"The ransomware gang paid me to make the file disappear. "
            "I left the password out so someone else would get the blame... "
            "but I couldn't fake my own badge.\""
        ),
        "clues": [
            {
                "icon": "🖥️",
                "name": "Server Log",
                "text": "The file was deleted at 2:17 AM using **Vikram's admin account**, from a computer inside the office.",
            },
            {
                "icon": "📝",
                "name": "Sticky Note",
                "text": "Vikram's admin password was found on a **sticky note** by the printer. Anyone could have used it.",
            },
            {
                "icon": "🚪",
                "name": "Front Door Log",
                "text": "**Vikram's ID badge** opened the office front door at 2:05 AM.",
            },
            {
                "icon": "📶",
                "name": "VPN Log",
                "text": "Sneha was connected **from home** all night. Nobody else used the VPN.",
            },
        ],
        "suspects": [
            {
                "name": "Vikram Singh",
                "emoji": "🧑‍💻",
                "role": "System Administrator",
                "personality": "Smug and confident",
                "answers": {
                    "where": "Asleep at home. I was in bed by midnight.",
                    "why": "I built that server myself. Why would I wreck my own work?",
                    "hiding": "My password got leaked, so anyone could log in as me! But my ID badge? Never leaves my side.",
                },
            },
            {
                "name": "Sneha Rao",
                "emoji": "🛡️",
                "role": "Security Analyst",
                "personality": "Logical",
                "answers": {
                    "where": "Working from home on the VPN. The logs will prove it.",
                    "why": "I was the one leading the investigation. Deleting it erases my own work.",
                    "hiding": "I noticed strange admin logins last week. I was about to report them.",
                },
            },
            {
                "name": "Arjun Das",
                "emoji": "👔",
                "role": "IT Manager",
                "personality": "Strict",
                "answers": {
                    "where": "On a late video call with our Singapore office until 3 AM.",
                    "why": "Honestly? I wanted this kept quiet. But destroying evidence? No.",
                    "hiding": "I told the team not to inform the CEO yet. That's poor judgment, not a crime.",
                },
            },
            {
                "name": "Ritika Sen",
                "emoji": "🧑‍🎓",
                "role": "Junior Developer",
                "personality": "Quiet and nervous",
                "answers": {
                    "where": "I left at midnight and took a cab home.",
                    "why": "I only joined three months ago! I barely know how the server works.",
                    "hiding": "I'm the one who found that sticky note. I put it back... I didn't know who to tell.",
                },
            },
        ],
    },
}
