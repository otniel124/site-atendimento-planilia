import streamlit as st
import pandas as pd
import time
import os
from datetime import datetime

ARQUIVO_CSV = "atendimentos.csv"

# Garante que o arquivo exista com cabeçalhos
if not os.path.exists(ARQUIVO_CSV):
    df_inicial = pd.DataFrame(columns=["Nome", "Motivo", "Data", "Horário", "Unidade"])
    df_inicial.to_csv(ARQUIVO_CSV, index=False)

st.title("📋 Sistema de Atendimento")

st.header("Novo Atendimento")
nome = st.text_input("Nome")
motivo = st.text_input("Motivo")
unidade = st.selectbox("Unidade", ["Unidade A", "Unidade B", "Unidade C"])

data_atual = datetime.now().strftime('%d/%m/%Y')
hora_atual = time.strftime('%H:%M:%S')
st.info(f"📅 Data: {data_atual} | 🕒 Horário atual: {hora_atual}")

if st.button("Registrar"):
    if nome and motivo:
        novo = pd.DataFrame([[nome, motivo, data_atual, hora_atual, unidade]],
                            columns=["Nome", "Motivo", "Data", "Horário", "Unidade"])
        novo.to_csv(ARQUIVO_CSV, mode='a', index=False, header=False)
        st.success(f"✅ Atendimento de {nome} registrado com sucesso!")
    else:
        st.warning("⚠️ Preencha nome e motivo.")

st.divider()

st.header("📄 Lista de Atendimentos")
df = pd.read_csv(ARQUIVO_CSV)
st.dataframe(df, use_container_width=True