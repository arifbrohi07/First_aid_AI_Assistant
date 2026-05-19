def emergency_check(disease):
    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "severe bleeding",
        "unconscious",
        "stroke",
        "heart attack"
    ]

    for keyword in emergency_keywords:
        if keyword.lower() in disease.lower():
            return """
⚠️ EMERGENCY WARNING:
Your symptoms may require immediate medical attention.
Go to nearest hospital or call emergency services NOW.
"""
    return None