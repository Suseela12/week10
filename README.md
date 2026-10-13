# Experiment 10 : Chain-of-Thought Prompting

## Aim
To compare direct prompting and step-by-step prompting on a multi-step mathematical word problem.

## Problem Statement
A farmer has 15 cows, buys 7 more cows, and then sells half of the total. Determine how many cows remain using two prompting methods.

## Technologies Used
- Python
- Google Gemini AI
- Google Gen AI SDK

## Prompting Methods

### 1. Direct Prompt
The original math problem is sent directly to the LLM.

### 2. Chain-of-Thought Prompt
The same problem is sent with an instruction to explain the calculations step by step.

## Algorithm
1. Initialize the Gemini API client.
2. Define the math word problem.
3. Send the direct prompt to the LLM.
4. Send the step-by-step prompt using the same model and parameters.
5. Extract the final answers.
6. Compare both answers with the expected result.
7. Display the comparison and analysis.
8. Save the results to a text file.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration
Set the `GEMINI_API_KEY` environment variable before running the program. Never upload API keys to GitHub.

## Execution

```bash
python src/main.py
```

## Expected Calculation
- Initial cows: 15
- After buying 7 cows: 15 + 7 = 22
- After selling half: 22 - 11 = 11

**Expected answer: 11 cows.**

## Expected Output
- Direct prompt and response.
- Step-by-step prompt and response.
- Extracted answers.
- Correctness comparison.
- Results saved in `output/cot_results.txt`.

## Result
The experiment compares direct and step-by-step prompting on the same reasoning task using a common expected answer.

## Conclusion
Step-by-step instructions can encourage a model to present intermediate calculations and make its answer easier to verify. However, they do not guarantee correctness, so the final answer must be checked against the expected result.


└── README.md
```
