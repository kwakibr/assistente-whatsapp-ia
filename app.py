import streamlit as st

# ── Configurações da página ─────────────────────────────
st.set_page_config(page_title="Assistente WhatsApp IA", layout="centered")
st.title("🤖 Assistente de Atendimento no WhatsApp")

st.markdown(
    """
    Este é um **exemplo funcional** do painel do seu bot de WhatsApp com IA.  
    Ele mostra como a IA vai responder seus clientes – sem menus numéricos, incentivando
    **teste grátis** antes de falar de preços.
    ---
    """,
    unsafe_allow_html=True,
)

# ── Estado do chat ──────────────────────────────────────
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "assistant", "content": "Oi! Tudo bem? 😊 Quer testar grátis nosso sistema de Canais, Filmes e Séries?"},
    ]

# ── Exibir histórico ────────────────────────────────────
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ── Entrada do usuário ──────────────────────────────────
msg = st.chat_input("Digite aqui…")
if msg:
    # mostra a mensagem do usuário
    st.session_state.chat.append({"role": "user", "content": msg})
    with st.chat_message("user"):
        st.markdown(msg)

    # lógica simples de resposta
    lower = msg.lower()
    if any(p in lower for p in ["preço", "valor", "quanto"]):
        answer = (
            "Planos disponíveis:\n"
            "• **Mensal:** R$ 24,90\n"
            "• **3 meses:** R$ 64,90\n"
            "• **6 meses:** R$ 97,90\n\n"
            "Mas antes, faça o **teste grátis** 😉\n"
            "Em qual dispositivo você quer assistir?"
        )
    else:
        answer = (
            "Legal! Nosso teste grátis funciona em Smart TV, TV Box, celular, "
            "PC ou notebook. Qual aparelho você prefere?"
        )

    # mostra a resposta
    st.session_state.chat.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
