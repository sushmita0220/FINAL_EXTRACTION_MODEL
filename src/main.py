from ocr_extractor import extract_text_from_pdf
from llm_parser import load_mistral_model, parse_invoice_with_mistral
from po_matcher import extract_gstin, fetch_pending_po, match_po
from tkinter import Tk, filedialog
import json

def main(model_path, json_schema):
    """
    Main execution flow with local file upload.
    """
    # Use a file dialog to upload the PDF
    Tk().withdraw()  # Hide the root window
    pdf_path = filedialog.askopenfilename(
        title="Select Invoice PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        print("No file selected. Exiting...")
        return

    print(f"Processing file: {pdf_path}")

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Load Mistral model
    llm = load_mistral_model(model_path)

    # Parse invoice text into JSON
    structured_data = parse_invoice_with_mistral(llm, text, json_schema)

    # Extract GSTIN and fetch POs
    gstin = extract_gstin(text)
    po_data = fetch_pending_po(gstin)

    # Match invoice with PO
    matched_po = match_po(structured_data['products_services'], po_data)

    # Output JSON
    output = {
        "invoice_data": structured_data,
        "po_match": matched_po
    }

    # Save output
    output_file = f"output/invoice_output.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)

    print(f"✅ Extracted data saved to {output_file}")

if __name__ == "__main__":
    MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q2_K.gguf"
    
    JSON_SCHEMA = {
        "invoice_number": "str",
        "invoice_date": "str",
        "supplier": "str",
        "products_services": [
            {
                "description": "str",
                "hsn_sac": "str",
                "quantity": "int",
                "unit": "str",
                "rate": "float",
                "total_price": "float"
            }
        ]
    }
    
    main(MODEL_PATH, JSON_SCHEMA)
