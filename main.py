import os 
from dotenv import load_dotenv
import argparse
from google import genai
from google.genai import types

#Load enviroment variables 
load_dotenv()

def generate_content(client: genai.Client, messages: list[types.Content]) -> tuple[int, int, str]:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents= messages,
    )

    if not response.usage_metadata: 
        raise RuntimeError("Gemini API response appears to be malformed")
    
    return (
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
        response.text,
        )

    

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    user_prompt = args.user_prompt

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None: 
        raise RuntimeError("Missing API key")

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    client = genai.Client(api_key=api_key)
    prompt_tokens, response_tokens, response_text = generate_content(client, messages)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(f"Response:") 
    print(response_text)
    




if __name__ == "__main__":
    main()
