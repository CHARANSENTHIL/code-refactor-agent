from agent.refactor_chain import chain, parser
from tools.file_reader import read_python_file

import json
import os
import re


print("Starting Refactor Agent...")

code = read_python_file("input/sample.py")

print("File Loaded")


response = chain.invoke({
    "code": code
})


print("Raw output received")

raw_text = response["text"]

print("MODEL OUTPUT:\n", raw_text)


# Extract JSON safely
match = re.search(r'\{.*\}', raw_text, re.DOTALL)

if not match:
    raise Exception("Model did not return JSON")


json_text = match.group()


# Parse with Pydantic
result = parser.parse(json_text)


output = {

    "before": code,

    "after": result.refactored_code,

    "code_smells": result.code_smells,

    "improvements": result.improvements,

    "explanation": result.explanation

}


os.makedirs("output", exist_ok=True)


with open("output/result.json", "w") as f:

    json.dump(output, f, indent=4)


print("\nDONE\n")

print(json.dumps(output, indent=4))
