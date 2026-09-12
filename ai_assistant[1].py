def generate_response(text):
    """
    Simple AI-style response generator.

    This module can later be connected to a real AI API
    such as OpenAI for more advanced responses.
    """

    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"

    if "python" in text:
        return (
            "Python is a popular programming language used for "
            "AI, automation, web development, and data science."
        )

    if "github" in text:
        return (
            "GitHub is a platform used to store, manage, "
            "and collaborate on software projects."
        )

    if "ai" in text or "artificial intelligence" in text:
        return (
            "AI enables computers to perform tasks that normally "
            "require human intelligence."
        )

    if "thank" in text:
        return "You're welcome! 😊"

    return (
        "That's interesting! Connect this project to a real AI model "
        "to generate more intelligent and contextual responses."
    )
