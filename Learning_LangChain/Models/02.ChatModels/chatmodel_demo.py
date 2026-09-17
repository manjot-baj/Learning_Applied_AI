from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4")

result = chat_model.invoke("What is the Capital of India")
print(result.model_dump_json(indent=2))
print(result.content)

"""
01. temperature usage 
range is 0 to 2
keeping 0 will provide same output for same input
and keep close to 0 for more factual, more similar and less creative output for same input
and keep close to 1.5 for more creative and different output for same input 

The temperature parameter in OpenAI's chat models controls the randomness of the model's responses. It essentially determines how creative or deterministic the output will be.
Low temperature (e.g., 0.2): The model's responses will be more focused and deterministic, sticking closely to the most likely next words. This is useful for tasks requiring precise and predictable answers.
High temperature (e.g., 0.8): The model's responses will be more diverse and creative, introducing more variability and less predictable outputs. This can be useful for creative writing or brainstorming.
For example, a temperature of 0 would make the model very deterministic, always choosing the highest probability next word, while a temperature of 1 would make the model more random and creative.

02. max completion tokens to manage tokens(words)
"""
chat_model = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=10)  # Low
chat_model = ChatOpenAI(
    model="gpt-4", temperature=1.8, max_completion_tokens=10
)  # High

result = chat_model.invoke("Suggest me 5 Indian male names")
result = chat_model.invoke("Give me Names of 5 Indian Revolutionaries")
result = chat_model.invoke("Write a essay on Indian Revolutionaries in English")
print(result.content)
