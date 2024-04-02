import os
import anthropic
from anthropic_client import create_anthropic_client
import notetaker

client = create_anthropic_client()

def send_message_test(input_message):
    message = client.messages.create(
        model="claude-3-sonnet-20240229", # Medium model used for testing
        max_tokens=1024,
        messages=[
            {"role": "user", "content": input_message}
        ]
    )

    # Formats the API response to just the bot's response message
    response_content = message.content[0].text
    return response_content

def main():
    pass





if "__name__" == "__main__":
    main()