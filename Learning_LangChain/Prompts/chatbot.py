from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model
chat_model = ChatOpenAI(model="gpt-4", temperature=0.1)

# Memory
chat_history = [
    SystemMessage(content="You are a helpful assistant"),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)
print(chat_history)
