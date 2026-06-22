import streamlit as st

# Configuration de la page
st.set_page_config(page_title="IA de Wanis", page_icon="🤖", layout="centered")

# Style CSS personnalisé pour rendre l'interface magnifique
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.markdown('<div class="main-title"> IA de Wanis 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Bienvenue dans ton espace de discussion et de contrôle</div>', unsafe_allow_html=True)

# Barre latérale (Sidebar) pour les options
with st.sidebar:
    st.header("⚙️ Configuration")
    st.write("Paramètres de l'application")
    mode = st.selectbox("Choisir le mode", ["Discussion principale", "Paramètres", "À propos"])
    st.success("Statut : Connecté au serveur")

# Contenu principal selon le mode sélectionné
if mode == "Discussion principale":
    st.subheader("💬 Chat avec l'IA")

    # Initialisation de l'historique des messages si elle n'existe pas
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Salut Wanis ! Comment je peux t'aider aujourd'hui ?"}
        ]

    # Affichage des messages de l'historique
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Zone de saisie pour l'utilisateur
    if user_input := st.chat_input("Écris ton message ici..."):
        # Ajouter le message de l'utilisateur à l'historique
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Réponse automatique de test (on pourra la connecter à une vraie IA plus tard)
        import google.generativeai as genai

# 1. On connecte le cerveau
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# 2. Quand l'utilisateur écrit, on envoie le message à Google
if user_input:
    response = model.generate_content(user_input)
    reply = response.text

    # 3. On affiche la réponse de l'IA
    with st.chat_message("assistant"):
        st.write(reply)
import streamlit as st
import google.generativeai as genai
elif mode == "Paramètres":
    st.subheader("⚙️ Panneau de contrôle")
    st.write("Modifie ici les options de ton application.")
    volume = st.slider("Volume de l'audio", 0, 100, 50)
    st.write(f"Volume réglé sur : {volume}%")

elif mode == "À propos":
    st.subheader("ℹ️ Informations")
    st.info("Cette application a été créée sur mesure pour Wanis et tourne localement sur le conteneur Linux du Chromebook.")
