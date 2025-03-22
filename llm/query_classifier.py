import redis
import json
from sentence_transformers import SentenceTransformer, util

# Load the pretrained model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Define categories and example queries
categories = {
    "contract": [
        "What is my contract value?",
        "When does my contract end?",
        "Show me the contract details.",
        "How much is paid to the?",
        "Vendor engagement.",
        "PO details",
        "Active PO for ",
        "Active Contracts",
        "Contract Expiry",
        "Count of POs",
        "Vendor engagement details.",
        "Invoice Paid",
        "Invoice Amount",
        "PO expiration date.",
        "Purchase order details.",
        "Contract renewal.",
        "Purchase Order renewal.",
        "PO renewal.",
        "Purchase Order Renewal."
    ],
    "software": [
        "What software do we have?",
        "Is X software available?",
        "List all approved software."
    ],
    "other": [
        "Tell me about AI.",
        "How does LangChain work?"
    ]
}

# Compute embeddings and store in Redis (if not already stored)
for category, examples in categories.items():
    if not redis_client.exists(category):  # Avoid recomputing if already in Redis
        embeddings = model.encode(examples, convert_to_tensor=False).tolist()
        redis_client.set(category, json.dumps(embeddings))

def classify_query(query):
    """
    Classifies a query using Redis cache.
    """
    query_key = f"query:{query}"
    cached_result = redis_client.get(query_key)

    if cached_result:
        print("Using cached result")
        return cached_result.decode("utf-8")  # Return cached category

    # Compute query embedding
    query_embedding = model.encode(query, convert_to_tensor=False).tolist()

    best_match = None
    highest_score = -1

    for category in categories.keys():
        stored_embeddings = json.loads(redis_client.get(category))
        similarity_scores = util.pytorch_cos_sim(query_embedding, stored_embeddings).max().item()

        if similarity_scores > highest_score:
            highest_score = similarity_scores
            best_match = category

    # Cache result for future queries
    result_category = best_match if highest_score > 0.5 else "other"
    redis_client.set(query_key, result_category)

    return result_category

# Example usage
if __name__ == "__main__":
    test_queries = [
        "Give me complete details of Smartsheet vendor engagement?",
        "When does my contract for Smartsheet expire?",
        "Do we have access to Jira?",
        "What is AI?"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        print(f"Classified as: {classify_query(query)}")
        print("-" * 40)