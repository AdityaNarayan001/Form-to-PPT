from ollama import chat
from system_prompt import system_prompt

def llm(prompt):
    response = chat(
        model='mistral',
        messages=[
            {'role': 'system', 'content': system_prompt,},
            {'role': 'user', 'content': prompt}
            ],
        stream=False,
    )

    return response['message']['content']