import streamlit as st
import pandas as pd
from dataclasses import dataclass
from typing import Dict
from datetime import datetime

# ============================================
# CONFIGURAÇÃO E CONSTANTES
# ============================================
st.set_page_config(page_title="Cálculo de Tempo de Trabalho", page_icon="⏱️", layout="wide")

PROCESS_DURATIONS = {'tipo_1': 5.91, 'tipo_2': 7.59, 'tipo_3': 0.85}
WORK_DAY_MINUTES = 510  # 8h30min

@dataclass
class ResultadoTempo:
    tempo_total_minutos: float
    tempo_tipo_1: float
    tempo_tipo_2: float
    tempo_tipo_3: float
    
    @property
    def horas_formatadas(self) -> str:
        h = int(self.tempo_total_minutos // 60)
        m = int(self.tempo_total_minutos % 60)
        s = int((self.tempo_total_minutos % 1) * 60)
        return f"{h}h {m}m {s}s"

# ============================================
# LÓGICA DE CÁLCULO
# ============================================
def calcular_tempo(n1, n2, n3):
    t1 = n1 * PROCESS_DURATIONS['tipo_1']
    t2 = n2 * PROCESS_DURATIONS['tipo_2']
    t3 = n3 * PROCESS_DURATIONS['tipo_3']
    total = t1 + t2 + t3
    return ResultadoTempo(round(total, 2), round(t1, 2), round(t2, 2), round(t3, 2))

# --- Inicialização do Estado (Para o botão Limpar) ---
if 'n1' not in st.session_state: st.session_state.n1 = 0
if 'n2' not in st.session_state: st.session_state.n2 = 0
if 'n3' not in st.session_state: st.session_state.n3 = 0

def limpar():
    st.session_state.n1 = 0
    st.session_state.n2 = 0
    st.session_state.n3 = 0

# ============================================
# INTERFACE
# ============================================
st.title("⏱️ Calculadora de Jornada")

tab1, tab2, tab3 = st.tabs(["🔢 Calculadora de Processos", "📝 Registro Avulso", "⚙️ Configurações"])

with tab1:
    st.header("Cálculo por Tipo de Processo")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        n1 = st.number_input("Tipo 1 (5.91 min)", min_value=0, step=1, key="n1")
    with col2:
        n2 = st.number_input("Tipo 2 (7.59 min)", min_value=0, step=1, key="n2")
    with col3:
        n3 = st.number_input("Tipo 3 (0.85 min)", min_value=0, step=1, key="n3")

    c_btn1, c_btn2 = st.columns([1, 5])
    with c_btn1:
        calcular = st.button("📊 Calcular", type="primary", use_container_width=True)
    with c_btn2:
        st.button("🗑️ Limpar Campos", on_click=limpar)

    if calcular:
        res = calcular_tempo(n1, n2, n3)
        st.divider()
        m1, m2, m3 = st.columns(3)
        m1.metric("Tempo Total", res.horas_formatadas)
        m2.metric("Total em Minutos", f"{res.tempo_total_minutos} min")
        
        diff = WORK_DAY_MINUTES - res.tempo_total_minutos
        if diff >= 0:
            m3.metric("Status", "✅ Dentro", f"+{int(diff)} min restantes")
            st.success(f"Você ainda tem {int(diff)} minutos de saldo na jornada.")
        else:
            m3.metric("Status", "⚠️ Excedido", f"{int(diff)} min", delta_color="inverse")
            st.warning(f"Atenção: Você excedeu a jornada em {abs(int(diff))} minutos.")

with tab2:
    st.header("Histórico e Análise")
    st.info("Aqui você poderá visualizar o gráfico de produtividade no futuro.")
    if 'res' in locals():
        df = pd.DataFrame({
            'Tipo': ['Tipo 1', 'Tipo 2', 'Tipo 3'],
            'Minutos': [res.tempo_tipo_1, res.tempo_tipo_2, res.tempo_tipo_3]
        })
        st.bar_chart(df.set_index('Tipo'))

with tab3:
    st.header("Configurações do Sistema")
    st.write(f"**Jornada Padrão:** {WORK_DAY_MINUTES} minutos (8h30)")
    st.write("**Versão:** 2.0 (Refatorada)")
