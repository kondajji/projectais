import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import KNeighborsClassifier

# Load a small, efficient model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Training data: Sample contract-related and software-related queries
queries = [
    "What is my contract value for Smartsheet?",
    "When does my Asana contract end?",
    "How much has been invoiced for Airtable?",
    "Which software is most used?",
    "What is the highest contract value?",
    "Show me software usage stats",
]

labels = ["contract", "contract", "contract", "software_usage", "contract", "software_usage"]

# Convert queries into embeddings
X_train = model.encode(queries)
y_train = np.array(labels)

# Train a simple classifier (K-Nearest Neighbors)
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(X_train, y_train)

def classify_query(query):
    """Classifies the query as 'contract' or 'software_usage' using embeddings."""
    query_embedding = model.encode([query])
    return clf.predict(query_embedding)[0]

# Example usage
if __name__ == "__main__":
    test_query = "When does my Smartsheet contract expire?"
    print(f"Query Type: {classify_query(test_query)}")
