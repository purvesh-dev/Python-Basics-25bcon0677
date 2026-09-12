from ai_assistant import generate_response


def main():
    print("🤖 AI Text Assistant")
    print("--------------------")
    print("Type 'exit' or 'quit' to close the assistant.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("AI: Goodbye! 👋")
            break

        if not user_input.strip():
            print("AI: Please enter something.")
            continue

        response = generate_response(user_input)
        print(f"AI: {response}")


if __name__ == "__main__":
    main()
