import fitz  # PyMuPDF
import json
import os

# Define paths
pdf_path = r"C:\Users\ROHIT\OneDrive\Desktop\Swayambhoo\pre_algebra_sample.pdf"
output_json_path = r"C:\Users\ROHIT\OneDrive\Desktop\Swayambhoo\extracted_examples.json"
image_output_dir = r"C:\Users\ROHIT\OneDrive\Desktop\Swayambhoo\extracted_images"

# Create directory for images
os.makedirs(image_output_dir, exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

examples = []
example_id = 1

# Iterate through pages
for page_num in range(len(doc)):
    page = doc[page_num]

    # Extract text as blocks (structured format)
    blocks = page.get_text("blocks")
    text = "\n".join([b[4] for b in sorted(blocks, key=lambda x: x[1])])  # Sorting by vertical position

    # Extract images
    image_list = page.get_images(full=True)
    image_paths = []

    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        img_ext = base_image["ext"]

        image_filename = f"example_{example_id}_{img_index}.{img_ext}"
        image_path = os.path.join(image_output_dir, image_filename)

        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        image_paths.append(image_path)

    # Process text to find Examples and Solutions
    lines = text.split("\n")
    question_text = []
    solution_text = []
    is_question = False
    is_solution = False

    for line in lines:
        line = line.strip()

        if "EXAMPLE" in line.upper():  # Improved detection (case insensitive)
            is_question = True
            is_solution = False
            question_text = [line]  # Reset question buffer
            solution_text = []  # Reset solution buffer
            continue

        if "SOLUTION" in line.upper():  # Improved detection
            is_solution = True
            is_question = False
            solution_text = [line]  # Reset solution buffer
            continue

        if is_question:
            question_text.append(line)

        if is_solution:
            solution_text.append(line)

    # Save Example only if both question and solution are found
    if question_text and solution_text:
        examples.append({
            "example_id": example_id,
            "question_text": " ".join(question_text).strip(),
            "question_images": image_paths,
            "solution_text": " ".join(solution_text).strip(),
            "solution_images": image_paths
        })
        example_id += 1

# Save the extracted data to JSON
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(examples, json_file, indent=4, ensure_ascii=False)

print(f"✅ Extraction complete. JSON file saved at: {output_json_path}")
print(f"📂 Images saved in: {image_output_dir}")
