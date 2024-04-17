# Getting Started with CHARLIE AI

Welcome to CHARLIE AI! This guide will walk you through setting up the project on your local machine and explain how to interact with the bot using the Anthropic API.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up the Anthropic API Key](#setting-up-the-anthropic-api-key)
- [Creating the Anthropic Client](#creating-the-anthropic-client)
- [Interacting with the Bot](#interacting-with-the-bot)
- [Try It Yourself](#try-it-yourself)
- [Expand and Customize](#expand-and-customize)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before getting started, make sure you have the following:

- Python 3.x installed on your system. You can download the latest version from the official Python website: https://www.python.org/downloads/
- An Anthropic API key (more on this later)

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/Stavdel/CHARLIE-AI
```

2. Navigate to the project directory:

```
cd CHARLIE-AI
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Setting Up the Anthropic API Key

To use the Anthropic API, you need to generate an API key. Follow these steps:

1. Go to the Anthropic API key settings page: https://console.anthropic.com/settings/keys
2. Click on "Generate New Key" and copy the generated API key.
3. Note: You will need credits to make API calls. You can get $5 of credits for free by verifying your phone number. Check out: https://console.anthropic.com/dashboard

Now, you need to set the API key as an environment variable on your system. Here's how to do it:

### For Windows:
1. Open the Start menu and search for "Environment Variables".
2. Click on "Edit the system environment variables".
3. Click on the "Environment Variables" button.
4. Under "User variables" or "System variables", click "New".
5. Set the variable name as `ANTHROPIC_API_KEY` and the value as your API key.
6. Click "OK" to save the changes.

### For macOS and Linux:
1. Open a terminal.
2. Open the shell configuration file (e.g., `.bashrc` or `.zshrc`) in a text editor.
3. Add the following line at the end of the file:

```
export ANTHROPIC_API_KEY="your_api_key_here"
```

4. Save the file and restart your terminal for the changes to take effect.

Note: Replace `your_api_key_here` with the actual API key you generated.

## Creating the Anthropic Client

To initialize the bot and access its functions, you need to create an Anthropic client. Here's the code snippet that creates the client:

```python
import os
import anthropic

def create_anthropic_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key is None:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")
    return anthropic.Anthropic(api_key=api_key)
```

This code is located in the `anthropic_client.py` file. It retrieves the API key from the environment variable and creates an instance of the Anthropic client.

Please note that using the Anthropic API calls will incur costs. If you need funding for this project, you can send an email to stavdeldev@gmail.com to request an API key at no charge. However, there may be limits on the number of API calls you can make per week.

## Interacting with the Bot

The `bot_interactions.py` file contains the necessary functions to send messages to the bot and receive its responses. Let's break down the code and explain each part.

```python
import os
import anthropic
from anthropic_client import create_anthropic_client
import notetaker

client = create_anthropic_client()

def send_message_test(input_message):
    message = client.messages.create(
        model="claude-3-sonnet-20240229",  # Medium model used for testing
        max_tokens=1024,
        messages=[
            {"role": "user", "content": input_message}
        ]
    )

    # Formats the API response to just the bot's response message
    response_content = message.content[0].text
    return response_content

def main():
    # Test for making a markdown file from the bot's responses.
    # Bot will then determine what the title should be then it will be made.
    response_content = send_message_test(input("User: "))
    print("Done")

if __name__ == "__main__":
    main()
```

1. First, the necessary modules are imported, including the `create_anthropic_client` function from the `anthropic_client.py` file.

2. The `send_message_test` function is defined, which takes an `input_message` as a parameter. This function is responsible for sending the message to the bot and receiving its response.

3. Inside the `send_message_test` function, the `client.messages.create` method is called with the following parameters:
   - `model`: The name of the model to use for generating the response. In this case, it's set to "claude-3-sonnet-20240229", which is a medium-sized model used for testing.
   - `max_tokens`: The maximum number of tokens (words or word pieces) allowed in the bot's response. It's set to 1024.
   - `messages`: A list containing a single message object, where the "role" is set to "user" and the "content" is the `input_message` provided by the user.

4. The bot's response is extracted from the API response using `message.content[0].text` and stored in the `response_content` variable.

5. The `response_content` is then returned by the `send_message_test` function.

6. The `main` function serves as the entry point of the script. It prompts the user for input using `input("User: ")` and passes the user's message to the `send_message_test` function.

7. The bot's response is stored in the `response_content` variable, and "Done" is printed to indicate that the interaction is complete.

To interact with the bot, you can run the `bot_interactions.py` script and enter your message when prompted. The bot will process your message and generate a response based on the provided model and parameters.

Note: The `notetaker` module is imported but not used in the provided code snippet as of now as it is for testing another script, so it is not needed yet. Make sure to handle any dependencies or remove the import if it's not needed.

## Try It Yourself

Now that you've set up the Anthropic client and learned how to send messages to the bot using the `send_message_test` function from the `bot_interactions.py` file, it's time to try it out on your own!

Here's a simple example to get you started. Create a new file called `example.py` in the same directory as `bot_interactions.py` and `anthropic_client.py`, and add the following code:

```python
from bot_interactions import send_message_test

def main():
    message = "Hello, CHARLIE AI! How are you doing today?"
    response = send_message_test(message)
    print("User:", message)
    print("Bot:", response)

if __name__ == "__main__":
    main()
```

In this example, we:

1. Import the `send_message_test` function from the `bot_interactions` module.

2. Define the `main` function, which serves as the entry point of the script.

3. Create a variable called `message` and assign it the value "Hello, CHARLIE AI! How are you doing today?". This is the message we want to send to the bot.

4. Call the `send_message_test` function, passing the `message` as an argument, and store the bot's response in the `response` variable.

5. Print the user's message and the bot's response using `print` statements, prefixing them with "User:" and "Bot:" respectively.

To run the `example.py` script, open a terminal or command prompt, navigate to the directory containing the files, and run the following command:

```
python example.py
```

The script will send the message "Hello, CHARLIE AI! How are you doing today?" to the bot and display the bot's response in the console.

Here's an example of what the output might look like:

```
User: Hello, CHARLIE AI! How are you doing today?
Bot: Hello! As an AI language model, I don't have feelings, but I'm functioning well and ready to assist you. Is there anything specific you'd like help with today?
```

Feel free to modify the `message` variable in the `example.py` script to send different messages to the bot and explore its capabilities.

## Expand and Customize

This is just a starting point! You can build upon this example and create your own custom scripts to interact with the bot in various ways. Here are a few ideas:

- Create a command-line interface that allows users to enter messages interactively and receive responses from the bot.
- Integrate the bot into a web application or chatbot interface.
- Experiment with different prompts and messages to explore the bot's knowledge and capabilities.
- Use the bot's responses to generate content, answer questions, or provide assistance in your own projects.

The possibilities are endless! Have fun exploring and creating your own unique interactions with CHARLIE AI.

## Troubleshooting

If you encounter any issues while setting up or interacting with CHARLIE AI, here are a few common problems and their solutions:

1. **Error: `ANTHROPIC_API_KEY` environment variable is not set.**
   - Make sure you have properly set the `ANTHROPIC_API_KEY` environment variable with your Anthropic API key. Double-check the instructions in the [Setting Up the Anthropic API Key](#setting-up-the-anthropic-api-key) section.

2. **Error: `ModuleNotFoundError: No module named 'anthropic'`**
   - Ensure that you have installed the required dependencies by running `pip install -r requirements.txt` in the project directory.

3. **The bot's responses are not what I expected.**
   - The bot's responses are generated based on the provided model and parameters. You can experiment with different models or adjust the `max_tokens` parameter in the `send_message_test` function to control the length of the responses.

If you encounter any other issues or have questions, feel free to open an issue on the project's GitHub repository or reach out to the project maintainer for assistance.

---
