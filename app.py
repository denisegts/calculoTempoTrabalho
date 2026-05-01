import streamlit as st
from dataclasses import dataclass
from typing import Dict, Tuple

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Cálculo de Tempo de Trabalho",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CONSTANTS
# ============================================
PROCESS_DURATIONS: Dict[str, float] = {
    'tipo_1': 5.91,    # minutes
    'tipo_2': 7.59,    # minutes
    'tipo_3': 0.85     # minutes
}

WORK_DAY_MINUTES: int = 510  # 8 hours and 30 minutes
WORK_DAY_HOURS: int = 8
WORK_DAY_EXTRA_MINUTES: int = 30


# ============================================
# CLASSES
# ============================================
@dataclass
class ResultadoTempo:
    """Stores and formats work time calculation results."""
    tempo_total_minutos: float
    tempo_tipo_1: float
    tempo_tipo_2: float
    tempo_tipo_3: float
    
    @property
    def horas(self) -> int:
        return int(self.tempo_total_minutos // 60)
    
    @property
    def minutos(self) -> int:
        return int(self.tempo_total_minutos % 60)
    
    @property
    def segundos(self) -> int:
        segundos_totais = int((self.tempo_total_minutos % 1) * 60)
        return segundos_totais
    
    @property
    def dentro_jornada(self) -> bool:
        return self.tempo_total_minutos <= WORK_DAY_MINUTES
    
    @property
    def diferenca_minutos(self) -> float:
        """Returns remaining time (negative if exceeds)."""
        return WORK_DAY_MINUTES - self.tempo_total_minutos


# ============================================
# VALIDATION FUNCTIONS
# ============================================
def validar_entrada(num_tipo_1: int, num_tipo_2: int, num_tipo_3: int) -> Tuple[bool, str]:
    """
    Validates input values.
    
    Args:
        num_tipo_1: Number of type 1 processes
        num_tipo_2: Number of type 2 processes
        num_tipo_3: Number of type 3 processes
    
    Returns:
        Tuple (valid: bool, message: str)
    """
    if num_tipo_1 < 0 or num_tipo_2 < 0 or num_tipo_3 < 0:
        return False, "❌ O número de processos não pode ser negativo!"
    
    if num_tipo_1 == 0 and num_tipo_2 == 0 and num_tipo_3 == 0:
        return False, "❌ Pelo menos um tipo de processo deve ser informado!"
    
    return True, "✅ Entrada validada com sucesso!"


# ============================================
# CALCULATION FUNCTIONS
# ============================================
def calcular_tempo_trabalho(num_tipo_1: int, num_tipo_2: int, num_tipo_3: int) -> ResultadoTempo:
    """
    Calculates total work time based on number of processes of each type.
    
    Args:
        num_tipo_1: Number of 5.91 minute processes
        num_tipo_2: Number of 7.59 minute processes
        num_tipo_3: Number of 0.85 minute processes
    
    Returns:
        ResultadoTempo with all calculations
    
    Raises:
        ValueError: If values are negative
    """
    valido, mensagem = validar_entrada(num_tipo_1, num_tipo_2, num_tipo_3)
    if not valido:
        raise ValueError(mensagem)
    
    tempo_tipo_1 = num_tipo_1 * PROCESS_DURATIONS['tipo_1']
    tempo_tipo_2 = num_tipo_2 * PROCESS_DURATIONS['tipo_2']
    tempo_tipo_3 = num_tipo_3 * PROCESS_DURATIONS['tipo_3']
    tempo_total = tempo_tipo_1 + tempo_tipo_2 + tempo_tipo_3
    
    return ResultadoTempo(
        tempo_total_minutos=round(tempo_total, 2),
        tempo_tipo_1=round(tempo_tipo_1, 2),
        tempo_tipo_2=round(tempo_tipo_2, 2),
        tempo_tipo_3=round(tempo_tipo_3, 2)
    )


# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.title("📊 Sobre o Projeto")
    
    st.markdown("""
    ### Cálculo de Tempo de Trabalho
    
    **Versão Web - Projeto 2 Refatorado**
    
    #### ✨ Características:
    - ✅ Type Hints para melhor legibilidade
    - ✅ Constantes extraídas (sem magic numbers)
    - ✅ Funções modulares e reutilizáveis
    - ✅ Validação robusta de entrada
    - ✅ Saída formatada e detalhada
    - ✅ Precisão de segundos
    
    #### 📋 Tipos de Processo:
    - **Tipo 1:** 5.91 minutos
    - **Tipo 2:** 7.59 minutos
    - **Tipo 3:** 0.85 minutos
    
    #### ⏱️ Jornada Padrão:
    - **8 horas e 30 minutos**
    - **510 minutos no total**
    
    ---
    
    **Desenvolvido com ❤️ por @denisegts**
    
    [GitHub](https://github.com/denisegts/calculoTempoTrabalho) | [Projeto 1](https://github.com/denisegts/calculoTempoTrabalho/blob/main/TRABALHO/Projeto1.ipynb) | [Projeto 2](https://github.com/denisegts/calculoTempoTrabalho/blob/projeto2-refactored/TRABALHO/Projeto2.ipynb)
    """)


# ============================================
# MAIN INTERFACE
# ============================================
st.title("📊 Cálculo de Tempo de Trabalho")
st.markdown("**Interface Web - Projeto 2 Refatorado**")
st.markdown("---")

# Input columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📝 Tipo 1")
    num_tipo_1 = st.number_input(
        "Processos Tipo 1 (5.91 min cada)",
        min_value=0,
        value=8,
        step=1,
        key="tipo1"
    )

with col2:
    st.subheader("📝 Tipo 2")
    num_tipo_2 = st.number_input(
        "Processos Tipo 2 (7.59 min cada)",
        min_value=0,
        value=10,
        step=1,
        key="tipo2"
    )

with col3:
    st.subheader("📝 Tipo 3")
    num_tipo_3 = st.number_input(
        "Processos Tipo 3 (0.85 min cada)",
        min_value=0,
        value=45,
        step=1,
        key="tipo3"
    )

st.markdown("---")

# Calculate
try:
    resultado = calcular_tempo_trabalho(num_tipo_1, num_tipo_2, num_tipo_3)
    
    # Results section
    st.subheader("⏱️ Resultado Final")
    
    # Main metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Tempo Total",
            value=f"{resultado.horas}h {resultado.minutos}m {resultado.segundos}s",
            delta=None
        )
    
    with col2:
        st.metric(
            label="Em Minutos",
            value=f"{resultado.tempo_total_minutos:.2f} min",
            delta=None
        )
    
    with col3:
        if resultado.dentro_jornada:
            diferenca = resultado.diferenca_minutos
            minutos_rest = int(diferenca)
            segundos_rest = int((diferenca % 1) * 60)
            status_text = f"✅ Dentro"
            delta_text = f"+{minutos_rest}m {segundos_rest}s"
        else:
            excesso = abs(resultado.diferenca_minutos)
            minutos_exc = int(excesso)
            segundos_exc = int((excesso % 1) * 60)
            status_text = f"⚠️ Excede"
            delta_text = f"-{minutos_exc}m {segundos_exc}s"
        
        st.metric(
            label="Status da Jornada",
            value=status_text,
            delta=delta_text
        )
    
    st.markdown("---")
    
    # Detailed breakdown
    st.subheader("📋 Detalhamento por Tipo de Processo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.write("**Tipo 1 (5.91 min/processo)**")
            st.write(f"Quantidade: {num_tipo_1}")
            st.write(f"Tempo: {resultado.tempo_tipo_1:.2f} min")
            st.write(f"Em horas: {resultado.tempo_tipo_1/60:.2f}h")
    
    with col2:
        with st.container():
            st.write("**Tipo 2 (7.59 min/processo)**")
            st.write(f"Quantidade: {num_tipo_2}")
            st.write(f"Tempo: {resultado.tempo_tipo_2:.2f} min")
            st.write(f"Em horas: {resultado.tempo_tipo_2/60:.2f}h")
    
    with col3:
        with st.container():
            st.write("**Tipo 3 (0.85 min/processo)**")
            st.write(f"Quantidade: {num_tipo_3}")
            st.write(f"Tempo: {resultado.tempo_tipo_3:.2f} min")
            st.write(f"Em horas: {resultado.tempo_tipo_3/60:.2f}h")
    
    st.markdown("---")
    
    # Status detail
    st.subheader("📊 Análise da Jornada")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.write("**Jornada Padrão**")
            st.write(f"Horas: {WORK_DAY_HOURS}h {WORK_DAY_EXTRA_MINUTES}m")
            st.write(f"Minutos: {WORK_DAY_MINUTES} min")
    
    with col2:
        if resultado.dentro_jornada:
            diferenca = resultado.diferenca_minutos
            minutos_rest = int(diferenca)
            segundos_rest = int((diferenca % 1) * 60)
            st.success(f"✅ Tempo restante: {minutos_rest}m {segundos_rest}s")
        else:
            excesso = abs(resultado.diferenca_minutos)
            minutos_exc = int(excesso)
            segundos_exc = int((excesso % 1) * 60)
            st.warning(f"⚠️ Tempo em excesso: {minutos_exc}m {segundos_exc}s")
    
    # Expandable sections
    with st.expander("📈 Visualizar Gráfico de Tempo por Tipo"):
        import pandas as pd
        
        data = {
            'Tipo': ['Tipo 1', 'Tipo 2', 'Tipo 3'],
            'Tempo (minutos)': [
                resultado.tempo_tipo_1,
                resultado.tempo_tipo_2,
                resultado.tempo_tipo_3
            ]
        }
        df = pd.DataFrame(data)
        
        st.bar_chart(df.set_index('Tipo'))
    
    with st.expander("📝 Ver Cálculo Detalhado"):
        st.write("""
        ### Fórmula Utilizada:
        ```
        Tempo Total = (Tipo 1 × 5.91) + (Tipo 2 × 7.59) + (Tipo 3 × 0.85)
        ```
        
        ### Seu Cálculo:
        """)
        st.code(f"""
Tipo 1: {num_tipo_1} × 5.91 = {resultado.tempo_tipo_1:.2f} min
Tipo 2: {num_tipo_2} × 7.59 = {resultado.tempo_tipo_2:.2f} min
Tipo 3: {num_tipo_3} × 0.85 = {resultado.tempo_tipo_3:.2f} min
────────────────────────────────
Total:                    {resultado.tempo_total_minutos:.2f} min
        """)

except ValueError as e:
    st.error(str(e))

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 12px;">
    <p>🚀 Aplicação desenvolvida com Streamlit | 
    📊 Dados precisos com Type Hints | 
    ✅ Validação robusta</p>
</div>
""", unsafe_allow_html=True)
