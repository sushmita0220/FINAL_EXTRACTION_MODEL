import pypdfium2 as pdfium
import pytesseract
from PIL import Image
from io import BytesIO

def convert_pdf_to_images(file_path, scale=300/72):
    """
    Convert PDF pages to images with improved resolution.
    """
    pdf_file = pdfium.PdfDocument(file_path)
    page_indices = [i for i in range(len(pdf_file))]
    renderer = pdf_file.render(page_indices, scale=scale)
    
    images = []
    for image in renderer:
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format="PNG")
        images.append(Image.open(BytesIO(img_byte_arr.getvalue())))
    
    return images

def extract_text(images):
    """
    Extracts text from images using OCR.
    """
    extracted_text = []
    for img in images:
        text = pytesseract.image_to_string(img)
        extracted_text.append(text)
    return "\n".join(extracted_text)
