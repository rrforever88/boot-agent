import os
from dotenv import load_dotenv
from openai import OpenAI

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
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
    ]
)

# Print number of tokens used by model

if response.usage == None:
    raise RuntimeError("API request failed")

print(f"""
Prompt tokens: {response.usage.prompt_tokens} 
Response tokens: {response.usage.completion_tokens}""")

print(response.choices[0].message.content)

def main():
    print("Hello from boot-agent!")


if __name__ == "__main__":
    main()
