#!/usr/bin/env python

import sys
import os
import argparse

# constants
SYSTEM_PROMPT = "You are an ancient code sage. Analyze this code for cursedness — bad naming, spaghetti logic, magic numbers, crimes against readability. Give it a curse rating from 1-10 with a dramatic verdict and specific callouts."
BRUTAL_PROMPT = "You are a merciless ancient code sage with no patience for mediocrity. Tear this code apart. Find every flaw, no matter how small. Be dramatic, be harsh, be unforgiving. Give it a curse rating from 1-10."
GEMINI_MODEL = "gemini-2.5-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

# function to ask gemini about the code
def ask_gemini(client, code, prompt):
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=code,
        config={
            "system_instruction": prompt
        }
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Is my code cursed?")
    parser.add_argument("file", help="File to analyze")
    parser.add_argument("--brutal", "-b", action="store_true", help="No mercy mode - harsher roasting")
    parser.add_argument("--output", "-o", help="Save report to file")
    parser.add_argument("--max-words", "-w", type=int, help="Max words in response")

    args = parser.parse_args()
    target = args.file
    output = args.output
    max_words = args.max_words

    if not API_KEY:
        print("is-my-code-cursed: error: GEMINI_API_KEY not set. run 'export GEMINI_API_KEY=\"<your_key>\"'")
        sys.exit(1)

    if os.path.isdir(target):
        print("is-my-code-cursed: error: directories are not supported")
        sys.exit(1)
    else:
        try:
            with open(target, "r") as f:
                code = f.read()

                # ONLY import here because genai is a huge lib
                # takes forever to load so things like --help take forever
                from google import genai
                client = genai.Client(api_key=API_KEY)
                try:
                    prompt = SYSTEM_PROMPT
                    if args.brutal:
                        prompt = BRUTAL_PROMPT
                    if max_words:
                        prompt += f" Keep your response under {max_words} words."
                    response = ask_gemini(client, code, prompt)
                except Exception as e:
                    print(f"is-my-code-cursed: error: Gemini API failed - {e}")
                    sys.exit(1)

                print(response)

                if output:
                    with open(output, "w") as out:
                        out.write(response)
        except FileNotFoundError:
            print("is-my-code-cursed: error: file not found")

if __name__ == "__main__":
    main()