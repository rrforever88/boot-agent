import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt}
]

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("No API KEY found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

# Print number of tokens used by model

if response.usage == None:
    raise RuntimeError("API request failed")

if args.verbose == True:
    print(f"""
    User prompt: {args.user_prompt}
    """)

    print(f"""
    Prompt tokens: {response.usage.prompt_tokens} 
    Response tokens: {response.usage.completion_tokens}""")

print(f"""
Response:
{response.choices[0].message.content}""")



def main():
    print("Hello from boot-agent!")


if __name__ == "__main__":
    main()
