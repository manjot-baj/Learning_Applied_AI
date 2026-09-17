from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import json
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Model
chat_model = ChatOpenAI(model="gpt-4", temperature=0.1)

# UI
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical",
    ],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# Load prompt template
with open("template.json", "r") as f:
    config = json.load(f)

template = PromptTemplate(**config)

# Summarize
if st.button("Summarize"):

    input_variable_mapping = {
        "length_input": length_input,
        "paper_input": paper_input,
        "style_input": style_input,
    }

    chain = template | chat_model

    result = chain.invoke(input_variable_mapping)

    st.write(result.content)
