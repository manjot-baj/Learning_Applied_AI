from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Mumbai is capital of Maharashtra"
    "Kolkata is capital of West Bengal"
    "Ahmedabad is capital of Gujrat"
]

result = embedding_model.embed_documents(documents)

print(str(result))
