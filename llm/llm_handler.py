import os
from langchain.tools import Tool
from llm.query_classifier import classify_query
from llm.response_synthesizer import synthesize_response
from llm.llama_contract_index import query_contract_details
from llm.vendor_name_extractor import extract_vendor_name

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Define contract lookup tool
contract_tool = Tool(
    name="contract_lookup",
    func=query_contract_details,
    description="Fetch contract details for a software vendor."
)

def handle_query(user_query):
    """Handles the user query by classifying, fetching data, and synthesizing a response."""
    
    # Step 1: Classify the query
    query_type = classify_query(user_query)
    print(f"Classified query as: {query_type}")

    # Step 2: Extract vendor name (when using llamaIndex it is not needed)
    #vendor_name = extract_vendor_name(user_query)
    #if not vendor_name:
    #    return "No vendor name detected. Please specify a software vendor."

    # Step 3: Fetch contract data if relevant
    contract_data = None
    if "contract" in query_type:
        contract_data = contract_tool.run(user_query)

    return synthesize_response(user_query, contract_data)

if __name__ == "__main__":
    test_queries = [
        "How many active PO do we have for Smartsheet?",
        "Give me complete details of Smartsheet vendor engagement.",
        "PO details Smartsheet",
        "When does my Airtable PO expire? If multiple POs exist, consider the latest one."
        "Do we have Contract for Figma?",
        "What is current PO status for Asana?"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        print("Response:")
        print(handle_query(query))
        print("-" * 50)
