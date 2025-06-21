import re
import json

# Convert to JSON
# Load the full text extracted from the PDF
def convert_to_json(file_path):
    with open("mainapp/data/"+file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract questions, choices, and answers using regex
    pattern = re.compile(
        r"(\d+)\.\s+(.*?)\n\s*A\.\s+(.*?)\n\s*B\.\s+(.*?)\n\s*C\.\s+(.*?)\n\s*D\.\s+(.*?)\n\s*Answer:\s*([A-D])",
        re.DOTALL
    )

    matches = pattern.findall(text)

    # Convert to desired JSON format
    questions_json = []
    for match in matches:
        q_number, question, a, b, c, d, answer_letter = match
        answer_map = {'A': a, 'B': b, 'C': c, 'D': d}
        choices = [f"A. {a}", f"B. {b}", f"C. {c}", f"D. {d}"]
        answer = f"{answer_letter}. {answer_map[answer_letter]}"
        questions_json.append({
            "question": question.strip(),
            "choices": choices,
            "answer": answer
        })

    # Save to a JSON file
    output_path = "water_climate_mcqs2.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions_json, f, indent=2)

# print(output_path)


# Extract from JSON
def access_json_data(file_path):
    with open('mainapp/data/'+file_path, 'r') as file:
        data = json.load(file)
    return data