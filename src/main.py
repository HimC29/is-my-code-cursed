#!/usr/bin/env python

import sys
import os
import argparse

# constants
SYSTEM_PROMPT = "You are an ancient code sage. Analyze this code for cursedness — bad naming, spaghetti logic, magic numbers, crimes against readability. Give it a curse rating from 1-10 with a dramatic verdict and specific callouts."
BRUTAL_PROMPT = "You are a merciless ancient code sage with no patience for mediocrity. Tear this code apart. Find every flaw, no matter how small. Be dramatic, be harsh, be unforgiving. Give it a curse rating from 1-10."
GEMINI_MODEL = "gemini-2.5-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

ignored_dirs = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv"
}

# check if a file is binary or text
def is_binary_file(file, chunk_size=1024):
    try:
        chunk = file.read(chunk_size)

        if b"\x00" in chunk:
            return True

        chunk.decode("utf-8")

        return False

    except UnicodeDecodeError:
        return True

# iterate text files
def iter_text_files(target):
    for dirpath, dirnames, filenames in os.walk(target):
        dirnames[:] = [
            d for d in dirnames
            if d not in ignored_dirs
        ]

        for filename in filenames:
            path = os.path.join(dirpath, filename)

            try:
                with open(path, "rb") as f:
                    if not is_binary_file(f):
                        yield path

            except Exception:
                continue

# function for printing and exiting
def error_exit(string, code):
    print("is-my-code-cursed: error: " + string)
    sys.exit(code)

def print_verbose(verbose, string):
    if verbose:
        print(string)

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
    parser.add_argument("--verbose", "-v", action="store_true", help="Print status when importing lib and calling API")
    parser.add_argument("--exclude", "-e", help="Comma-seperated directories to ignore")

    args = parser.parse_args()
    target = args.file
    output = args.output
    max_words = args.max_words
    verbose = args.verbose
    excludes = args.exclude.split(",") if args.exclude else []

    for exclude in excludes:
        ignored_dirs.add(exclude)

    if not API_KEY:
        error_exit("GEMINI_API_KEY not set. run 'export GEMINI_API_KEY=\"<your_key>\"'", 1)

    code = ""

    if os.path.isdir(target):
        for path in iter_text_files(target):
            with open(path, "r") as f:
                code += f"File: {path}\n{f.read()}"
    else:
        try:
            with open(target, "r") as f:
                code = f.read()
        except FileNotFoundError:
            error_exit("file not found", 1)

    # ONLY import here because genai is a huge lib
    # takes forever to load so things like --help take forever
    print_verbose(verbose, "loading Google genai lib")
    from google import genai
    client = genai.Client(api_key=API_KEY)
    try:
        prompt = SYSTEM_PROMPT
        if args.brutal:
            prompt = BRUTAL_PROMPT
        if max_words:
            prompt += f" Keep your response under {max_words} words."
        print_verbose(verbose, "Calling Gemini API\n")
        response = ask_gemini(client, code, prompt)
    except Exception as e:
        error_exit(f"Gemini API failed - {e}", 1)

    print(response)

    if output:
        with open(output, "w") as out:
            out.write(response)

if __name__ == "__main__":
    main()