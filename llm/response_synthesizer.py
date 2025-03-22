from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from utils.config import get_openai_api_key
from llama_index.core import Response
import os


os.environ["TOKENIZERS_PARALLELISM"] = "false"


openai_api_key = get_openai_api_key()
llm = ChatOpenAI(model="gpt-4", temperature=0.5, openai_api_key=openai_api_key)

# Define summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["question", "output"],
    template="""
    Given the following contract details, that could be either extracted from a database:
    {output}
    or a response of a model {output}. Understand the Question, data format and provide a summary of the relevant details.Do not repeat same message.
    Summarize the relevant details based on this user question: "{question}". 
    Provide a clear, concise response that directly answers the question. 
    If the vendor name is not found, return: " No relevant contract details found or Vendor not part of the inventory".
    """
)

def synthesize_response(question, output):
    """
    Uses an LLM to generate a natural summary of contract details based on the query.
    """
    print("Output is:", output)

    if isinstance(output, Response):
        response = llm.invoke(summary_prompt.format(question=question, output=str(output)))  # ✅ Use `output`

    elif not output or output.strip() == "":
        return "No contract details available for the requested vendor."
    
    else:
        response = llm.invoke(summary_prompt.format(question=question, output=output))  # ✅ Use `output`
    
    return response.content  # Extracts only the model's text response

