import streamlit as st
import time

st.set_page_config(page_title="Sistema de Atendimento", layout="centered")

fila_atendimentos = []

st.title("🧾 Sistema de Atendimento Online")

with st.form("adicionar_atendimento"):
    nome = st.text_input("Nome do cliente")
    motivo = st.text_input("Motivo do atendimento")
    enviado = st.form_submit_button("➕ Adicionar Atendimento")

    if enviado and nome and motivo:
        horario = time.strftime('%H:%M:%S')
        atendimento = {"nome": nome, "motivo": motivo, "horario": horario}
        fila_atendimentos.append(atendimento)
        st.success(f"✅ Atendimento de {nome} adicionado com sucesso!")

st.subheader("📋 Fila de Atendimentos")
if fila_atendimentos:
    for i, a in enumerate(fila_atendimentos, 1):
        st.write(f"{i}. {a['nome']} - {a['motivo']} (às {a['horario']})")
else:
    st.info("Fila vazia.")

if st.button("✅ Atender próximo cliente"):
    if fila_atendimentos:
        a = fila_atendimentos.pop(0)
        st.success(f"👥 Atendendo {a['nome']} - Motivo: {a['motivo']} (às {a['horario']})")
    else:
        st.warning("Nenhum atendimento na fila.")
