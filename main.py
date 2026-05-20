import os 
from dotenv import load_dotenv
import argparse
from google import genai
from google.genai import types

#Load enviroment variables 
load_dotenv()


def main():
    print("Hello from ai-agent!")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None: 
        raise RuntimeError("Missing API key")

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.5-flash', contents= messages
    )
    if response.usage_metadata is None: 
        raise RuntimeError("Failed API request")

    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")



if __name__ == "__main__":
    main()
