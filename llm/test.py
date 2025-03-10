
from db import fetch_contract_details

from llm.query_classifier2 import classify_query

from llm.vendor_name_extractor import extract_vendor_name

import sys
import os
from langchain.tools import Tool

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# check Vendor Name extraction is working

if __name__ == "__main__":
    test_queries = [
        "What is my contract value for Smartsheet?"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        vendor_name = extract_vendor_name(query)
        print(f"Vendor Name: {vendor_name}")






