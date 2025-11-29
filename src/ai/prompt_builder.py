# constructs the AI prompt

def build_idea_prompt(topic: str, num_ideas: int, creativity: int) -> str:
    """
    Returns a perfectly crafted prompt for generating startup ideas.
    You will use this prompt inside api_client.py
    """
    return f"""
    You are a visionary entrepreneur like Elon Musk, Steve Jobs, and Vitalik Buterin combined.

Generate exactly {num_ideas} bold, original, and realistic startup ideas about: {topic}

Creativity level: {creativity}/10
- 1/10 = very safe and boring
- 10/10 = completely insane but technically possible and world-changing

Rules:
- One idea per line
- Start each idea with a number followed by a period (example: 1. ...)
- Keep each idea under 20 words
- No introductions, no conclusions, no explanations — only the numbered list

Examples of good output:
1. Self-healing solar panels using synthetic biology
2. AI therapist that charges per laugh
3. Underground data centers cooled by bitcoin mining heat
"""