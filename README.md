# Mistral Invoice Processor

A PDF invoice processing system using the Mistral 7B LLM model to extract structured data from invoice PDFs and match them with purchase orders.

## Overview

This project provides an end-to-end solution for processing invoice PDFs and matching them with corresponding purchase orders. It uses the Mistral 7B Instruct model (quantized to run on CPU) to extract structured data from invoices, then matches the extracted data with pending purchase orders using advanced matching algorithms.

## Features

- **PDF Text Extraction**: Extracts text from PDF invoices with OCR fallback for scanned documents
- **Structured Data Extraction**: Uses Mistral 7B LLM to convert unstructured invoice text into structured JSON
- **Purchase Order Matching**: Matches invoice items with pending purchase orders
- **Advanced Matching Algorithms**: Uses multiple matching strategies based on quantity, price, and description
- **Data Normalization**: Processes and normalizes extracted data for consistent output

## Requirements

- Python 3.7+
- Google Colab (for the notebook implementation)
- Internet connection (for downloading the Mistral model)

## Dependencies

The project requires several Python libraries:

- PyPDF2
- pytesseract
- pdf2image
- Pillow
- langchain
- llama-cpp-python
- requests
- difflib

System dependencies:
- tesseract-ocr
- poppler-utils

## Installation

The code is designed to run in Google Colab, which handles the installation of required dependencies. The setup process includes:

1. Installing system dependencies:
   ```
   apt-get update && apt-get install -y tesseract-ocr poppler-utils
   ```

2. Installing Python libraries:
   ```
   pip install pypdf2 langchain llama-cpp-python pytesseract pdf2image Pillow requests difflib
   ```

3. Downloading the Mistral 7B model:
   ```
   wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q2_K.gguf
   ```

## Usage

### Basic Processing

To process an invoice PDF:

1. Run the setup function to install dependencies and download the model:
   ```python
   setup_environment()
   ```

2. Process the invoice with:
   ```python
   process_invoice_pdf()
   ```

3. Upload your invoice PDF when prompted

### PO Matching Processing

To process an invoice and match with purchase orders:

1. Run the setup function:
   ```python
   setup_environment()
   ```

2. Process the invoice with PO matching:
   ```python
   process_invoice_pdf_with_po_matching()
   ```

3. Upload your invoice PDF when prompted

## How It Works

### Invoice Text Extraction

1. The PDF is first processed to extract embedded text
2. If no embedded text is found, OCR is used as a fallback

### Structured Data Extraction

1. The extracted text is sent to the Mistral 7B LLM with a specific prompt
2. The model extracts structured information including:
   - Invoice number
   - Invoice date
   - Seller details
   - Buyer details
   - Product/service details
   - Tax information
   - Total amount

### PO Matching

1. The GSTIN is extracted from the structured invoice data
2. The API is queried to fetch pending PO items for the extracted GSTIN
3. Each invoice item is matched with PO items using:
   - Quantity matching
   - Price matching
   - Description similarity
4. The best matching PO is identified for each invoice item

## Output

The system generates a JSON file containing:
- Party ID
- Invoice number
- Invoice date
- Matched items (with PO numbers)
- Discount information
- Currency

## API Configuration

For the PO matching functionality, the following API configuration is used:
- Base URL: http://uat.xserp.in/erp/purchase/json/po/pending_po_report/
