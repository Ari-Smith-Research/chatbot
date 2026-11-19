import streamlit as st
import os

st.write("LLM_BASE_URL", st.secrets["colab_url"])
st.write("GROQ_APR_KEY", st.secrets["groq_api_key"])

# Point to Colab tunnel URL for custom fine-tuned model, or Groq API as default/fallback
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.groq.com/openai/v1")
MODEL_NAME = "CIDS734-Lab8-model.Q4_K_M.gguf"

# Automatic fallback provider when Colab session is inactive
FALLBACK_BASE_URL = "https://api.groq.com/openai/v1"
FALLBACK_API_KEY = os.getenv("GROQ_API_KEY", "")
FALLBACK_MODEL_NAME = "llama-3.1-3b-instant"
