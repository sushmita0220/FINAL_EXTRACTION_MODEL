import requests

def extract_gstin(text):
    """
    Extract GSTIN from text.
    """
    import re
    gstin_pattern = r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}'
    match = re.search(gstin_pattern, text)
    return match.group(0) if match else None

def fetch_pending_po(gstin):
    """
    Fetch pending POs through API call.
    """
    API_URL = "http://uat.xserp.in/erp/purchase/json/po/pending_po_report/"
    response = requests.get(f"{API_URL}?gstin={gstin}")
    
    if response.status_code == 200:
        return response.json()
    return {}

def match_po(invoice_items, po_items):
    """
    Match invoice items with pending POs.
    """
    matched = []
    for item in invoice_items:
        for po in po_items:
            if item['description'] == po['description']:
                matched.append({
                    "invoice_item": item,
                    "po_item": po
                })
    return matched
