# ------------------------------
# 📁 File Paths and Directories
# ------------------------------
PDF_DIR = "data/invoices"                  # Path to invoice PDFs
MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q2_K.gguf"  # Path to local Mistral model
OUTPUT_DIR = "output"                      # Output directory for JSON files

# ------------------------------
# 🛠️ Model Configuration
# ------------------------------
N_CTX = 2048                               # Context window size
TEMPERATURE = 0.7                          # Model temperature (controls creativity)
MAX_TOKENS = 1024                          # Max tokens for output
TOP_P = 0.9                                # Nucleus sampling

# ------------------------------
# 🌐 API Configuration
# ------------------------------
# API URL for fetching pending POs
PO_API_URL = "https://your-po-api.com/get_pending_po"

# API authentication keys (if required)
PO_API_KEY = "YOUR_SECRET_API_KEY"         # Replace with your API key

# Timeout settings for API calls
API_TIMEOUT = 30                           # Timeout in seconds

# ------------------------------
# 🛡️ Security and Error Handling
# ------------------------------
# Retry settings for API requests
RETRY_ATTEMPTS = 3
RETRY_DELAY = 5                            # Delay in seconds between retries

# ------------------------------
# 🛠️ OCR Settings
# ------------------------------
OCR_LANGUAGE = "eng"                       # Language for OCR
OCR_SCALE = 300 / 72                       # DPI scaling factor
