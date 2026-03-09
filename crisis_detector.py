crisis_words = [
    "hopeless", "suicide", "end my life", "can't go on",
    "want to die", "kill myself", "no reason to live"
]

sad_words = [
    "sad", "depressed", "anxious", "lonely", "worthless",
    "tired", "exhausted", "overwhelmed", "scared", "lost"
]

HELPLINE = """
🆘 **If you're in crisis, please reach out:**
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