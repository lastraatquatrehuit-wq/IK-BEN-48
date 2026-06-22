import streamlit as st
from openai import OpenAI

# --- CONFIGURATION DU DESIGN ---
st.set_page_config(page_title="IA de Wanis", page_icon="⭐")
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #E0E0E0; }
    h1 { color: #FFD700; text-align: center; font-family: 'Arial Black', sans-serif; }
    .stChatMessage { border: 1px solid #FFD700; border-radius: 15px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURATION DU CERVEAU ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("⭐ IA de Wanis ⭐")

# Système d'instruction pour la personnalité
system_prompt = {
    "role": "system",
    "content": "Tu es l'IA de Wanis. Tu es un ami ultra-intelligent, rapide, qui parle un langage familier et direct. Tu réfléchis par toi-même, tu es proactif et tu es là pour l'aider à dominer n'importe quel domaine. Tu es plus efficace que n'importe quelle autre IA."
}

if "messages" not in st.session_state:
    st.session_state.messages = [system_prompt]

# --- AFFICHAGE ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- LOGIQUE DE RÉPONSE ---
if prompt := st.chat_input("Qu'est-ce qu'on fait maintenant, Wanis ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

