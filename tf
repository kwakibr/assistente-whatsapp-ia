import streamlit as st
from PIL import Image
import requests, json, os

st.set_page_config(page_title="Assistente WhatsApp IA", page_icon="🤖", layout="wide")
st.title("🤖 Assistente de Atendimento – WhatsApp")

# ─── interface simples ──────────────────────────────────────────────
with st.sidebar:
    st.header("Configurações")
    openai_key = st.text_input("🔑 OPENAI_API_KEY", type="password")
    whatsapp_number = st.text_input("📱 Seu número (com DDI+DDD)", value="+556499335171")
    if st.button("Salvar"):
        st.success("Configurações salvas (mantidas apenas nesta sessão).")

st.write("""Esta é uma **simulação** da IA que responderá seus clientes no WhatsApp.
No WhatsApp real ela seguirá o mesmo estilo de resposta sem menus numéricos.
""")

# ─── chat demo (texto) ───────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()
with chat_container:
    for m in st.session_state.messages:
        st.chat_message(m["role"]).write(m["content"])

prompt = st.chat_input("Envie sua mensagem…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # regra fixa: teste grátis antes de preços
    if any(p in prompt.lower() for p in ["preço", "valor", "quanto"]):
        answer = (
            "Temos 3 opções de plano:\n"
            "• **Mensal** – R$ 24,90\n"
            "• **3 meses** – R$ 64,90\n"
            "• **6 meses** – R$ 97,90\n\n"
            "Mas antes de decidir, faça o **teste grátis** 😉. "
            "Me diga em qual dispositivo você gostaria de assistir?"
        )
    else:
        answer = (
            "Oi! Tudo bem? 😊  Temos teste grátis de Canais, Filmes e Séries. "
            "Gostaria de testar? Funciona em Smart TV, TV Box, celular, notebook…"
        )

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
streamlit==1.34.0
Pillow
