from pdf_processor import convert_pdf_to_images, extract_text
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from PDF, uses OCR fallback if embedded text fails.
    """
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = "".join([page.extract_text() or "" for page in reader.pages])
        
        # Use OCR fallback if embedded text is missing
        if not text.strip():
            images = convert_pdf_to_images(pdf_path)
            text = extract_text(images)
        
        return text

    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""
