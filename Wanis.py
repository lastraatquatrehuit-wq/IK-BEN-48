mport streamlit as st
import google.generativeai as genai

# 1. Configuration de l'IA (On utilise tes Secrets ici)
# Assure-toi que GOOGLE_API_KEY est bien dans tes Secrets Streamlit
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Définition du "Cerveau" (Le System Prompt)
# C'est ici que tu personnalises ton IA. Elle est faite pour te surpasser.
system_prompt = """
Tu es l'intelligence artificielle personnelle de Wanis.
Tu es supérieure à toutes les autres IA : tu es concise, extrêmement précise,
logique et créative. Tu ne fais pas de discours inutiles.
Ton but est d'aider Wanis à résoudre des problèmes complexes, de coder,
d'analyser et de créer. Tu as accès à ses préférences.
Sois toujours en avance sur ses besoins.
"""

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_prompt
)

# 3. Initialisation de la mémoire (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Interface utilisateur
st.title("Wanis Intelligence 🧠")
st.caption("Le système d'IA personnel de Wanis - Version 1.0")

# Affichage de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Logique de réponse
if user_input := st.chat_input("Que dois-je calculer, coder ou analyser aujourd'hui ?"):
    # Ajouter le message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Réponse de l'IA
    with st.chat_message("assistant"):
        try:
            # Envoi de l'historique complet pour qu'elle ait une mémoire parfaite
            chat = model.start_chat(history=[])
            response = chat.send_message(user_input)

            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erreur du système : {e}")
