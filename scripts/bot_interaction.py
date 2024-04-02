import os
import anthropic
from anthropic_client import create_anthropic_client

client = create_anthropic_client()

def send_message_test(input_message):
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": input_message}
        ]
    )

    # Formats the API response to just the bot's response message
    response_content = message.content[0].text
    return response_content

def main():
    user_input = input("User: ")
    response = "Charlie: " + send_message_test(user_input)
    print(response)

    # Used for testing... remove later.
    main()

if __name__ == "__main__":
    main()