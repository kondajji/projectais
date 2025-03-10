from llm.query_classifier import classify_query
from langchain.tools import Tool
from db.fetch_contract_details import get_contract_details
from llm.vendor_name_extractor import extract_vendor_name
from llm.response_synthesizer import synthesize_response  # Import new function
import os

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Define contract tool
contract_tool = Tool(
    name="contract_lookup",
    func=get_contract_details,
    description="Fetch contract details for a software vendor."
)

# Agent function
def agent(query):
    """
    Determines the query type, retrieves data, and synthesizes a natural response.
    """
    query_type = classify_query(query)
    print(f"Query Type: {query_type}")

    vendor_name = extract_vendor_name(query)
    if not vendor_name:
        return " No vendor name detected. Please specify a software vendor."

    if "contract" in query_type:
        contract_details = contract_tool.run(vendor_name)
        return synthesize_response(query, contract_details)  # Call LLM response generator

    return "Sorry, I couldn't understand your request. Please ask about contract details."

if __name__ == "__main__":
    test_queries = [
        "give me complete details of Smartsheet vendor engagement?",
        "When does my Airtable PO expire?",
        "Has my Asana contract been renewed?",
        "How much have I paid for Autodesk?"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        print("Response:")
        print(agent(query))
        print("-" * 50)
