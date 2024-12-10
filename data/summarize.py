import os
import json


def combine_paragraphs(contents):
    combined_content = []
    current_paragraph = []

    for item in contents:
        if item["type"] == "p":
            current_paragraph.append(item["text"])
        else:
            if current_paragraph:
                combined_content.append(
                    {"type": "p", "text": " ".join(current_paragraph)}
                )
                current_paragraph = []
            combined_content.append(item)

    # If there's any paragraph left at the end, add it
    if current_paragraph:
        combined_content.append({"type": "p", "text": " ".join(current_paragraph)})

    return combined_content


def process_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for page in data["pages"]:
        page["content"] = combine_paragraphs(page["content"])

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def process_all_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            process_json_file(file_path)


# Assuming the script is in the same directory as the JSON files
directory_path = "."  # Or specify a different path
process_all_json_files(directory_path)
