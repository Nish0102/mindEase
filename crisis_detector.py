# List of words that indicate a crisis situation
crisis_words = [
    "hopeless", "suicide", "end my life", "can't go on",
    "want to die", "kill myself", "no reason to live",
    "better off dead", "can't take it anymore"
]

# List of words that indicate sadness
sad_words = [
    "sad", "depressed", "anxious", "lonely", "worthless",
    "tired", "exhausted", "overwhelmed", "scared", "lost",
    "hopeless", "empty", "numb", "broken", "hurt"
]

# Helpline message shown during crisis
HELPLINE = """
🆘 **Please reach out for immediate help:**
- **iCall (India):** 9152987821
- **Vandrevala Foundation:** 1860-2662-345 (24/7)
- **AASRA:** 9820466627
"""

def detect_mood(message: str) -> str:
    message = message.lower()
    if any(word in message for word in crisis_words):
        return "CRISIS"
    elif any(word in message for word in sad_words):
        return "SAD"
    else:
        return "NEUTRAL"
