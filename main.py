import os 
from dotenv import load_dotenv
import argparse
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions

#Load enviroment variables 
load_dotenv()

config = types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

def generate_content(client: genai.Client, messages: list[types.Content], verbose: bool):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config = config
    )

    if not response.usage_metadata: 
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if verbose is True:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
   

    

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
    
    generate_content(client, messages, args.verbose)
    





if __name__ == "__main__":
    main()
