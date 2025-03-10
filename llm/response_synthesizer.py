from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from utils.config import get_openai_api_key
import os


os.environ["TOKENIZERS_PARALLELISM"] = "false"


openai_api_key = get_openai_api_key()
llm = ChatOpenAI(model="gpt-4", temperature=0.5, openai_api_key=openai_api_key)

# Define summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["question", "sql_output"],
    template="""
    Given the following contract details extracted from a database:

    {sql_output}

    Summarize the relevant details based on this user question: "{question}".

    Provide a clear, concise response that directly answers the question. 
    If the vendor name is not found, return: " No relevant contract details found or Vendor not part of the inventory".
    """
)

def synthesize_response(question, sql_output):
    """
    Uses an LLM to generate a natural summary of contract details based on the query.
    """
    if not sql_output or sql_output.strip() == "":
        return "No contract details available for the requested vendor."

    response = llm.invoke(summary_prompt.format(question=question, sql_output=sql_output))
    return response.content  # Extracts only the model's text response
