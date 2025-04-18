from transformers import pipeline

generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")

prompt = """
You are an expert Python developer. Your task is to generate a Python function that meets the following requirements:

1. The function must prompt the user to enter two numbers.
2. It must also ask the user to enter an operation (+, -, *, /).
3. It must handle errors if the user enters non-numeric data.
4. It should convert the numbers to integers and perform the chosen operation.
5. It must use a `try-except` block to handle input errors.
6. If the user enters invalid input, prompt them again until they provide valid numbers.
7. If the user enters an invalid operation, display an error message and prompt again.
8. The function should be neatly formatted and use proper Python naming conventions.
9. Write only valid Python code, no explanations or comments.

Generate only the function definition, without extra text.
"""

generated_code = generator(prompt, max_length=1000, do_sample=False)[0]["generated_text"]

start_index = generated_code.find("def ")
if start_index != -1:
    generated_code = generated_code[start_index:]  

with open("generated_operations_code.py", "w") as file:
    file.write(generated_code)

print("Generated Python code saved to 'generated_operations_code.py'.")
