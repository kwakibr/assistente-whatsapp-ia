import streamlit as st
from datetime import datetime

# Configuração do layout da página
st.set_page_config(page_title="Assistente de Atendimento no WhatsApp", page_icon="🤖", layout="centered")

# Estilo escuro personalizado
st.markdown("""
    <style>
        body {
            background-color: #0e0e0e;
            color: #ffffff;
        }
        .stTextInput > div > div > input {
            background-color: #1e1e1e;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Título e mensagem principal
st.title("🤖 Assistente de Atendimento no WhatsApp")
st.markdown("Este é um exemplo funcional do painel do seu bot de WhatsApp com IA.  \n"
            "**Ele mostra como a IA vai responder seus clientes – sem menus numéricos,**  \n"
            "**incentivando teste grátis antes de falar de preços.**")

# Mensagem inicial
st.chat_message("assistant").markdown("Oi! Tudo bem? 😊  \nQuer testar grátis nosso sistema de Canais, Filmes e Séries?")

# Entrada do usuário (chat)
if prompt := st.chat_input("Digite aqui..."):
    st.chat_message("user").markdown(prompt)

    # IA simulada com respostas personalizadas
    if "preço" in prompt.lower():
        resposta = "Antes de falar de valores, que tal testar grátis nosso sistema? 😉"
    elif "teste" in prompt.lower() or "grátis" in prompt.lower():
        resposta = "Claro! Para liberar o teste, me envie o nome da sua TV ou aparelho (Ex: Smart TV, Android TV, TV Box)."
    elif "oi" in prompt.lower() or "tudo bem" in prompt.lower():
        resposta = "Oi! Tudo ótimo por aqui. Como posso te ajudar? 😄"
    elif "como funciona" in prompt.lower():
        resposta = "Você recebe acesso exclusivo a canais, filmes, séries e muito mais direto na sua TV ou celular."
    else:
        resposta = "Legal! Pode me contar mais sobre o que está procurando? 😊"

    st.chat_message("assistant").markdown(resposta)
