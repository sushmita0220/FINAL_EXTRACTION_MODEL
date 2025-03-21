# FINAL_EXTRACTION_MODEL
🛠️ Mistral Invoice Extractor
📌 Description
The Mistral Invoice Extractor is an AI-powered solution that automates invoice processing by:

Extracting structured data from invoice PDFs.
Using Mistral-7B LLM for local text parsing (no external LLM API calls).
Fetching pending PO data via API calls.
Generating structured JSON output with matched PO details.
Easily deployable using Docker.
⚙️ Features
✅ PDF to Image conversion using pypdfium2
✅ OCR-based text extraction with pytesseract
✅ LLM-powered structured data extraction with Mistral-7B
✅ PO matching via external API
✅ JSON output generation
✅ Modular architecture for easy scalability
📁 Project Structure
graphql
Copy
Edit
📂 MistralInvoiceExtractor
 ┣ 📂 src
 ┃ ┣ 📜 __init__.py                   # Package initialization
 ┃ ┣ 📜 pdf_processor.py              # PDF to Image & Text Extraction
 ┃ ┣ 📜 ocr_extractor.py              # OCR + Text Extraction
 ┃ ┣ 📜 llm_parser.py                 # Mistral LLM Integration
 ┃ ┣ 📜 po_matcher.py                 # PO Matching via API
 ┃ ┣ 📜 main.py                       # Main Execution Script
 ┣ 📂 config                          # Configuration files
 ┃ ┣ 📜 config.py                     # API keys, paths, parameters
 ┣ 📂 models                          # LLM model weights
 ┣ 📂 output                          # Extracted JSON output
 ┣ 📜 requirements.txt                # Python dependencies
 ┣ 📜 Dockerfile                      # Docker configuration
 ┣ 📜 .gitignore                      # Ignore unnecessary files
 ┣ 📜 README.md                       # Documentation
🛠️ Installation and Setup
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/MistralInvoiceExtractor.git
cd MistralInvoiceExtractor
2️⃣ Install dependencies
Create a virtual environment and install dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🚀 Running the Application
✅ Step 1: Place your PDF invoice in the /input folder.

✅ Step 2: Run the app:

bash
Copy
Edit
python src/main.py
✅ Step 3: Output JSON will be saved in /output:

json
Copy
Edit
{
    "invoice_data": {
        "invoice_number": "INV-12345",
        "invoice_date": "2025-03-21",
        "supplier": "ABC Pvt Ltd",
        "products_services": [
            {
                "description": "BI METAL CLAMP BODY",
                "hsn_sac": "7616",
                "quantity": 8000,
                "unit": "Nos",
                "rate": 10080,
                "total_price": 112000
            }
        ]
    },
    "po_match": [
        {
            "invoice_item": "BI METAL CLAMP BODY",
            "po_item": "CLAMP BODY",
            "matched": true
        }
    ]
}
🐳 Running with Docker
To run the solution inside a Docker container:

Build the Docker image
bash
Copy
Edit
docker build -t mistral-invoice-extractor .
Run the container
bash
Copy
Edit
docker run -v $(pwd)/output:/app/output mistral-invoice-extractor
🔥 API Configuration
The solution fetches pending PO reports using an external API.
You can configure the API URL in config/config.py:
python
Copy
Edit
API_URL = "https://your-po-api.com/get_pending_po"
⚙️ Environment Variables
Create a .env file in the root directory with the following variables:
ini
Copy
Edit
API_KEY=<YOUR_API_KEY>
API_URL=https://your-po-api.com/get_pending_po
⚙️ Dependencies
List of required Python libraries:

nginx
Copy
Edit
pypdfium2
pytesseract
Pillow
requests
langchain
jsonformer
🚀 Deployment Instructions
To deploy:

Push the project to GitHub
bash
Copy
Edit
git add .
git commit -m "Initial commit"
git push origin main
Deploy using Docker or on a server
Use Docker Compose for multi-container deployment if needed.
Deploy on AWS EC2, GCP, or Azure.
✅ Usage Instructions
Upload an invoice PDF to the /input folder.
Run the app using main.py.
The system extracts and processes the invoice.
The final JSON output is saved in /output.
🛠️ Future Improvements
🔥 Add support for multiple invoice layouts.
🔥 Improve PO matching accuracy.
🔥 Integrate a web-based UI for easy interaction.
