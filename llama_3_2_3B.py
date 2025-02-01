import re
import json
import torch
from transformers import pipeline


def toJson(json_string):
    json_string = json_string.strip()
    pattern = re.compile(r"^```json(.*)```$", flags=re.DOTALL)
    match = re.match(pattern, json_string)
    if match:
        print(match.group(1))
        return json.loads(match.group(1))
    return None


def llama_init():
    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    return pipe


def explain_solution(problem_statement, solution_code):
    pipe = llama_init()

    messages = [
            {"role": "system", "content": """
        1. Provide a summary of the problem.
        2. Explain the approach used in the solution code.
        3. Analyze the time complexity of the solution code.
        
        Please provide only Json format strings. 
        Provide the answers in JSON format with the following keys:
        - summary: summary of the problem.
        - approach: Explanation of the approach used.
        - complexity: Time complexity of the solution.
        - explain: Explain the solution code.
        
        Note:
        You should give a json response to the system.
        No response should be given other than summary, approach, complexity, and explain in json format.
        """
        },
        {"role": "user", "content": f"""
        Problem Description:
        {problem_statement}
    
        Solution Code:
        {solution_code}
            """
            },
    ]

    outputs = pipe(
        messages,
        max_new_tokens=512,
    )
    # print(outputs[0]["generated_text"][-1])
    res = outputs[0]["generated_text"][-1]
    if not res or not res['content']:
        return None
    return toJson(res['content'])
