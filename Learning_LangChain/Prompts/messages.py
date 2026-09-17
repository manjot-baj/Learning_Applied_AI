from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model
chat_model = ChatOpenAI(model="gpt-4", temperature=0.1)

# Chat-history

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain"),
]

result = chat_model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
