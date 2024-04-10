import base64
import json

def pdf_to_base64(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")
    return pdf_base64

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'Dokumentasi OCR sparepart.pdf'

try:
    base64_encoded_pdf = pdf_to_base64(pdf_file_path)
    
    # Create a JSON dictionary
    pdf_dict = {
        "filename": pdf_file_path,
        "base64": base64_encoded_pdf
    }

    # Convert the dictionary to JSON format
    json_data = json.dumps(pdf_dict, indent=2)
    
    with open("test.json", 'w') as f:
        f.write(json_data)
    
    # Print the JSON data
    print("JSON representation:")
    print(json_data)
except FileNotFoundError:
    print(f"Error: File '{pdf_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
