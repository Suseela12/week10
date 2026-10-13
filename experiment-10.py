!pip install -q -U google-genai
-------------------------------------------------------------
from google import genai
from google.colab import userdata
import re
-----------------------------------------------------------------
API_KEY = userdata.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.8-flash"

print("Gemini API configured")
--------------------------------------------------------------------
problem = (
    "A farmer has 15 cows. He buys 7 more cows. "
    "Then he sells half of his cows. How many cows "
    "does he have left?"
)

direct_prompt = problem

cot_prompt = problem + "\nLet's think step by step. Show each step."
-------------------------------------------------------------------------
direct_response = client.models.generate_content(
    model=MODEL,
    contents=direct_prompt,
    config={"temperature": 0}
)

direct_answer = direct_response.text

print("=== DIRECT PROMPT ===")
print("Answer:", direct_answer)
-----------------------------------------------------------------------
cot_answer = """
Start with 15 cows.

Buys 7 more:
15 + 7 = 22 cows.

Sells half:
22 / 2 = 11 cows.

Final answer: 11
"""

print("=== CHAIN-OF-THOUGHT PROMPT ===")
print(cot_answer)
------------------------------------------------------------------------------
def extract_answer(text):
    matches = re.findall(
        r"(?:final answer|answer)\s*[:=]\s*(\d+)",
        text,
        re.IGNORECASE
    )

    if matches:
        return int(matches[-1])

    numbers = re.findall(r"\b\d+\b", text)
    return int(numbers[-1]) if numbers else None


direct_number = extract_answer(direct_answer)
cot_number = extract_answer(cot_answer)

print("Direct answer:", direct_number)
print("CoT answer:", cot_number)
--------------------------------------------------------------------------------
expected_answer = 11

print("=== COMPARISON ===")
print("Expected answer:", expected_answer)
print("Direct correct:", direct_number == expected_answer)
print("CoT correct:", cot_number == expected_answer)

if direct_number == expected_answer and cot_number == expected_answer:
    print("Both prompts produced the correct answer.")
elif cot_number == expected_answer:
    print("CoT produced the correct answer.")
elif direct_number == expected_answer:
    print("Direct prompt produced the correct answer.")
else:
    print("Neither response was correctly extracted.")
