from langchain_openai import ChatOpenAI

from langchain.prompts import PromptTemplate
from utils.config import get_openai_api_key

# Load LLM
llm = ChatOpenAI(
    model="gpt-4",  # You can change this to Mistral/Llama
    temperature=0.2,
    openai_api_key=get_openai_api_key()
)

# Prompt to extract vendor name
vendor_extraction_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    Extract the software or vendor name from this query:
    "{query}"
    
    If no vendor is found, return "None". Just return the name, no explanations.
    """
)

def extract_vendor_name(query):
    """
    Uses an LLM to extract the vendor/software name from a query.
    """
    response = llm.invoke(vendor_extraction_prompt.format(query=query))
    return response.content if response.content.lower() != "none" else None
