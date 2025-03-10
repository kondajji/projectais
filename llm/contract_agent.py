import os
import sqlite3
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain.agents import AgentType
from dotenv import load_dotenv


# Load OpenAI API Key from environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("⚠️ OpenAI API Key is missing. Check your .env file!")
DB_PATH = "db/ais.db"

def fetch_contract_details(vendor_name):
    """Fetch contract details for a given vendor."""
    query = """
    SELECT vendor_name, start_date, end_date, contract_value, invoiced_amount, payment_status, contract_status, renewal_date
    FROM contracts
    WHERE vendor_name = ?;
    """
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, (vendor_name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        vendor, start_date, end_date, value, invoiced, payment_status, status, renewal = result
        return (f"📌 Contract Details for {vendor}:\n"
                f"- Start Date: {start_date}\n"
                f"- End Date: {end_date}\n"
                f"- Contract Value: ${value}\n"
                f"- Invoiced Amount: ${invoiced}\n"
                f"- Payment Status: {payment_status}\n"
                f"- Contract Status: {status}\n"
                f"- Renewal Date: {renewal if renewal else 'No renewal scheduled'}")
    else:
        return f"❌ No contract details found for {vendor_name}."

# Define the contract tool for LangChain
contract_tool = Tool(
    name="Contract Lookup",
    func=fetch_contract_details,
    description="Use this tool to fetch contract details for a software vendor. Input: Vendor Name."
)

# Initialize LangChain Agent
llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)

agent = initialize_agent(
    tools=[contract_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = input("Ask about a contract (e.g., 'What are my contract details for Asana?'): ")
    response = agent.run(query)
    print(response)
