from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4")

result = chat_model.invoke("What is the Capital of India")
print(result.model_dump_json(indent=2))
print(result.content)

"""
01. temperature usage 
low(less creative more direct factual) 
to 
high (more creative and less factual) 
02. max completion tokens to manage tokens(words)
"""
chat_model = ChatOpenAI(
    model="gpt-4", temperature=0.5, max_completion_tokens=10
)  # Low
chat_model = ChatOpenAI(
    model="gpt-4", temperature=1.8, max_completion_tokens=10
)  # High

result = chat_model.invoke("Suggest me 5 Indian male names")
result = chat_model.invoke("Give me Names of 5 Indian Revolutionaries")
result = chat_model.invoke("Write a essay on Indian Revolutionaries in English")
print(result.content)
