# Invoice Processing Solution with Mistral LLM

A Python-based solution for automated invoice data extraction, processing, and Purchase Order (PO) matching using the Mistral 7B LLM model.

## Overview

This solution automates the extraction of structured data from invoice PDFs and matches them with pending Purchase Orders. It uses the following technologies:

- **Mistral 7B Instruct**: A lightweight LLM model for invoice text analysis and data extraction
- **OCR (Tesseract)**: For extracting text from scanned invoice PDFs 
- **PO Matching API**: For matching extracted invoice data with pending purchase orders

## Features

- PDF text extraction with OCR fallback for scanned documents
- Structured invoice data extraction including:
  - Invoice number and date
  - Seller and buyer details with GSTIN
  - Line item details (description, quantity, price, HSN codes)
  - Tax information (CGST, SGST)
  - Total amounts
- Purchase Order matching based on:
  - GSTIN identification
  - Intelligent product matching using quantity, price, and description similarity
  - Flexible matching algorithms to handle real-world variations


## 🏗️ Project Structure

```
📂 MistralInvoiceExtractor
 ┣ 📂 src
 ┃ ┣ 📜 __init__.py                   
 ┃ ┣ 📜 pdf_processor.py              
 ┃ ┣ 📜 ocr_extractor.py              
 ┃ ┣ 📜 llm_parser.py                 
 ┃ ┣ 📜 po_matcher.py                 
 ┃ ┣ 📜 main.py                       
 ┣ 📂 config                          
 ┃ ┣ 📜 config.py                     
 ┣ 📂 models                          
 ┣ 📂 output                          
 ┣ 📜 requirements.txt                
 ┣ 📜 Dockerfile                     
 ┣ 📜 .gitignore                     
 ┣ 📜 README.md                       
```

## Prerequisites

- Python 3.8+
- 8GB+ RAM (recommended for Mistral model)
- CUDA-compatible GPU (optional, for faster processing)
- Internet connection (for API access)

## Installation

### Option 1: Google Colab (Easiest)

1. Open a new Google Colab notebook
2. Copy and paste the provided code
3. Run the setup_environment() function to download required dependencies
4. Run the main processing function

### Option 2: Local Installation

1. Clone the repository
```bash
git clone https://github.com/katanaml/llm-mistral-invoice-cpu
cd llm-mistral-invoice-cpu
```

2. Install the dependencies
```bash
pip install -r requirements.txt
```

3. Download the Mistral model
```bash
mkdir -p models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q2_K.gguf -P models
```

4. Install system dependencies
```bash
# For Ubuntu/Debian
sudo apt-get update && sudo apt-get install -y tesseract-ocr poppler-utils

# For macOS
brew install tesseract poppler
```

## Usage

### Basic Invoice Processing

```python
# Import the main processing function
from mistral_invoice_processor import process_invoice_pdf

# Run the invoice processor
process_invoice_pdf()
```

### Invoice Processing with PO Matching

```python
# Import the PO matching processor
from mistral_invoice_processor import process_invoice_pdf_with_po_matching

# Run the invoice processor with PO matching
process_invoice_pdf_with_po_matching()
```

## Deployment Options

### Option 1: Web Service with Flask

1. Create a Flask application to wrap the processor:

```python
from flask import Flask, request, jsonify
import io
from mistral_invoice_processor import extract_text_from_pdf, process_invoice_with_mistral

app = Flask(__name__)

@app.route('/process-invoice', methods=['POST'])
def process_invoice():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if file and file.filename.endswith('.pdf'):
        pdf_content = file.read()
        invoice_text = extract_text_from_pdf(pdf_content)
        if invoice_text:
            result = process_invoice_with_mistral(invoice_text)
            return jsonify(result)
        else:
            return jsonify({"error": "Failed to extract text from PDF"}), 500
    else:
        return jsonify({"error": "Invalid file format. Please upload a PDF."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

2. Deploy with Docker:

Create a Dockerfile:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create model directory and download model
RUN mkdir -p models
RUN wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q2_K.gguf -P models

# Copy application code
COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

3. Build and run:
```bash
docker build -t invoice-processor .
docker run -p 5000:5000 invoice-processor
```

### Option 2: Cloud Function / Lambda

1. Create handlers for AWS Lambda or Google Cloud Functions
2. Package the dependencies with the function
3. Set appropriate memory allocation (minimum 2GB recommended)
4. Configure API Gateway or HTTP trigger

### Option 3: Scheduled Batch Processing

For processing invoices in batches:

1. Set up a folder structure for incoming/processed invoices
2. Create a script to monitor the folders and process new files
3. Schedule the script using cron or a scheduler
4. Integrate with email/notification systems for results

## API Configuration

To use the PO matching functionality, configure the API details:

```python
# PO API configuration
BASE_URL = "http://your-api-endpoint.com/path"
API_KEY = "your-api-key"

# Initialize the processor
processor = IntegratedPOInvoiceProcessor(BASE_URL, API_KEY)
```

## Customization

### Adjusting the Prompt

The extraction quality can be customized by modifying the prompt in the `process_invoice_with_mistral` function:

```python
prompt = f"""
<instruction>
Extract structured invoice data into a JSON object from the provided invoice text. Use EXACTLY the following format and field names:
...
</instruction>
<invoice_text>
{invoice_text}
</invoice_text>
"""
```

### Model Parameters

You can adjust the Mistral model parameters for better performance:

```python
llm = LlamaCpp(
    model_path="models/mistral-7b-instruct-v0.1.Q2_K.gguf",
    temperature=0.0,  # Lower for more deterministic results
    max_tokens=4000,  # Adjust based on your needs
    n_ctx=4096,       # Context window size
    n_batch=512,      # Processing batch size
    f16_kv=True,      # Enables half-precision for better performance
)
```

## Troubleshooting

- **OCR Issues**: For poor quality scans, try adjusting Tesseract parameters
- **Memory Errors**: Reduce batch size or use a smaller model
- **Invoice Number Extraction**: Modify regex patterns to match your specific invoice number format
- **PO Matching Failures**: Adjust the matching thresholds in the processor class

