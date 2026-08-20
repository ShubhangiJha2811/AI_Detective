CASES = {

    "The Midnight Heist": {

        "id": "case_001",

        "title": "The Midnight Heist",

        "difficulty": "Easy",

        "location": "TechNova Research Lab",

        "victim": "Dr. Arjun Mehta",

        "time": "11:45 PM",

        "description": """
Dr. Arjun Mehta was working late inside the TechNova Research Lab.

At 11:45 PM, the laboratory security system detected
a sudden power interruption.

When the electricity returned, a highly valuable
AI prototype had disappeared.

Only four people had legitimate access to the laboratory that night.

The laboratory door was locked when security arrived.

Your mission is to determine who stole the prototype.
""",

        "solution": {

            "culprit": "Rohan Malhotra",

            "reason": (
                "Rohan was facing serious financial problems "
                "and planned to sell the AI prototype "
                "to a competitor."
            ),

            "method": (
                "He used his maintenance access card "
                "during the power outage."
            ),

            "key_evidence": [
                "His access card was used at 11:46 PM.",
                "He lied about being in the parking area.",
                "A backup camera captured his jacket near the laboratory."
            ]
        }
    },


    "The Vanishing Necklace": {

        "id": "case_002",

        "title": "The Vanishing Necklace",

        "difficulty": "Medium",

        "location": "Royal Heritage Hotel",

        "victim": "Mrs. Kapoor",

        "time": "9:30 PM",

        "description": """
A rare diamond necklace belonging to Mrs. Kapoor
disappeared during a private dinner.

The necklace had been placed inside
a locked display case.

There were four guests and one hotel employee
who could potentially access the display room.

Your mission is to discover who stole the necklace.
""",

        "solution": {

            "culprit": "Ananya Sharma",

            "reason": (
                "Ananya was facing financial problems "
                "and planned to sell the necklace."
            ),

            "method": (
                "She secretly created a duplicate "
                "of the display-case key."
            ),

            "key_evidence": [
                "Her fingerprints were found on the inner display handle.",
                "A duplicate key had been created.",
                "She gave contradictory statements about visiting the display room."
            ]
        }
    },


    "The Deleted File": {

        "id": "case_003",

        "title": "The Deleted File",

        "difficulty": "Hard",

        "location": "CyberCore Solutions",

        "victim": "CyberCore Security Team",

        "time": "2:17 AM",

        "description": """
CyberCore Solutions was investigating
a major ransomware attack.

At 2:17 AM, the main investigation file
was permanently deleted.

Only four employees had administrative
access to the server.

The attacker also attempted to remove
the access logs.

Your mission is to identify the person
responsible for deleting the investigation.
""",

        "solution": {

            "culprit": "Vikram Singh",

            "reason": (
                "Vikram was secretly working "
                "with the ransomware group."
            ),

            "method": (
                "He used a privileged administrator "
                "account to delete the investigation."
            ),

            "key_evidence": [
                "His administrator account accessed the server at 2:17 AM.",
                "His workstation was active at exactly 2:17 AM.",
                "Authentication logs were deliberately removed."
            ]
        }
    }
}